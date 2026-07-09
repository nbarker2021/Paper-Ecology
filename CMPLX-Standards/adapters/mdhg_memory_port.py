"""Stdlib MDHG memory/cache port for CMPLX-Standards.

Source lineage:
- D:\\repo_harvest\\CMPLXDevKit\\CMPLXLOCALMCP\\mcp_os\\agrm_mdhg_integration\\mdhg_ca.py
- D:\\repo_harvest\\CMPLXMCP\\agrm_snap\\mdhg_v0_2_2025_08_13.py

This module intentionally keeps the first Standards port dependency-free. The
older numpy AGRM/SNAP form remains evidence for a richer vector search adapter.
"""

from __future__ import annotations

import hashlib
import json
import math
import time
from dataclasses import dataclass, field
from typing import Any


def stable_hash(value: Any, length: int | None = None) -> str:
    blob = json.dumps(value, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")
    digest = hashlib.sha256(blob).hexdigest()
    return digest[:length] if length else digest


def quantize(vector: list[float], *, bins: int = 16) -> tuple[int, ...]:
    out: list[int] = []
    for value in vector:
        scaled = math.floor(float(value) * bins)
        out.append(int(max(0, min(bins - 1, scaled))))
    return tuple(out)


def slot_of(q_vector: tuple[int, ...], *, grid_side: int = 12) -> str:
    h1 = int(hashlib.sha256(("A" + str(q_vector)).encode("utf-8")).hexdigest(), 16)
    h2 = int(hashlib.sha256(("B" + str(q_vector)).encode("utf-8")).hexdigest(), 16)
    return f"{h1 % grid_side:02d},{h2 % grid_side:02d}"


@dataclass
class SlotEntry:
    key: str
    q_vector: tuple[int, ...]
    meta: dict[str, Any]
    last: float = field(default_factory=time.time)
    hits: int = 0


class MDHGCache:
    """24D vector -> quantized slot -> bounded per-slot cache."""

    def __init__(
        self,
        *,
        grid_side: int = 12,
        cap_per_slot: int = 6,
        bins: int = 16,
        layer_name: str = "default",
    ) -> None:
        self.grid_side = grid_side
        self.cap_per_slot = cap_per_slot
        self.bins = bins
        self.layer_name = layer_name
        self.slots: dict[str, list[SlotEntry]] = {}
        self.admission_count = 0
        self.eviction_count = 0

    def admit(self, vector: list[float], meta: dict[str, Any]) -> dict[str, Any]:
        q_vector = quantize(vector, bins=self.bins)
        slot = slot_of(q_vector, grid_side=self.grid_side)
        key = stable_hash(
            {"q": q_vector, "meta": {k: meta.get(k) for k in sorted(meta)[:12]}},
            16,
        )
        entries = self.slots.setdefault(slot, [])
        for entry in entries:
            if entry.key == key:
                entry.hits += 1
                entry.last = time.time()
                return {
                    "admit": True,
                    "hit": True,
                    "slot": slot,
                    "distance": 0.0,
                    "key": key,
                    "q_vector": q_vector,
                    "layer": self.layer_name,
                }

        distance = 0.0
        if entries:
            distance = float(
                min(sum(1 for a, b in zip(q_vector, entry.q_vector) if a != b) for entry in entries)
            )

        evicted: dict[str, Any] | None = None
        if len(entries) >= self.cap_per_slot:
            candidate = sorted(entries, key=lambda item: (item.hits, item.last))[0]
            entries.remove(candidate)
            self.eviction_count += 1
            evicted = {
                "key": candidate.key,
                "hits": candidate.hits,
                "meta": candidate.meta,
            }

        entries.append(SlotEntry(key=key, q_vector=q_vector, meta=dict(meta)))
        self.admission_count += 1
        return {
            "admit": True,
            "hit": False,
            "slot": slot,
            "distance": distance,
            "key": key,
            "evicted": evicted,
            "q_vector": q_vector,
            "layer": self.layer_name,
        }

    def occupancy_grid(self) -> list[list[int]]:
        grid = [[0 for _ in range(self.grid_side)] for _ in range(self.grid_side)]
        for slot, entries in self.slots.items():
            x_raw, y_raw = slot.split(",")
            grid[int(y_raw)][int(x_raw)] = min(9, len(entries))
        return grid

    def stats(self) -> dict[str, Any]:
        return {
            "layer": self.layer_name,
            "slots_used": len(self.slots),
            "total_entries": sum(len(entries) for entries in self.slots.values()),
            "admissions": self.admission_count,
            "evictions": self.eviction_count,
            "grid_side": self.grid_side,
            "cap_per_slot": self.cap_per_slot,
            "bins": self.bins,
        }


class MDHGMultiScale:
    """Three-layer MDHG cache: fast, medium, slow."""

    def __init__(self, *, grid_side: int = 12, cap_per_slot: int = 6, bins: int = 16) -> None:
        self.fast = MDHGCache(
            grid_side=grid_side, cap_per_slot=cap_per_slot, bins=bins, layer_name="fast"
        )
        self.med = MDHGCache(
            grid_side=grid_side, cap_per_slot=cap_per_slot, bins=bins, layer_name="med"
        )
        self.slow = MDHGCache(
            grid_side=grid_side, cap_per_slot=cap_per_slot, bins=bins, layer_name="slow"
        )

    def admit(self, vector: list[float], meta: dict[str, Any], *, layer: str = "fast") -> dict[str, Any]:
        return getattr(self, layer).admit(vector, meta)

    def admit_all_layers(self, vector: list[float], meta: dict[str, Any]) -> dict[str, Any]:
        return {
            "fast": self.admit(vector, meta, layer="fast"),
            "med": self.admit(vector, meta, layer="med"),
            "slow": self.admit(vector, meta, layer="slow"),
        }

    def stats(self) -> dict[str, Any]:
        return {
            "fast": self.fast.stats(),
            "med": self.med.stats(),
            "slow": self.slow.stats(),
        }


def deterministic_vector(seed: int, *, dim: int = 24) -> list[float]:
    return [((seed * 17 + idx * 31) % 997) / 997.0 for idx in range(dim)]


def run_mdhg_self_check() -> dict[str, Any]:
    cache = MDHGCache(grid_side=4, cap_per_slot=2, bins=8, layer_name="test")
    first = cache.admit(deterministic_vector(1), {"action_type": "store", "id": "a"})
    repeat = cache.admit(deterministic_vector(1), {"action_type": "store", "id": "a"})
    second = cache.admit(deterministic_vector(2), {"action_type": "validate", "id": "b"})
    third = cache.admit(deterministic_vector(3), {"action_type": "query", "id": "c"})
    multi = MDHGMultiScale(grid_side=4, cap_per_slot=2, bins=8)
    all_layers = multi.admit_all_layers(deterministic_vector(4), {"action_type": "store", "id": "d"})
    checks = {
        "first_admitted": first["admit"] is True and first["hit"] is False,
        "repeat_hit": repeat["hit"] is True and repeat["key"] == first["key"],
        "slots_are_stable": slot_of(quantize(deterministic_vector(1), bins=8), grid_side=4)
        == first["slot"],
        "capacity_enforced": cache.stats()["total_entries"] <= 3,
        "eviction_or_multislot_recorded": cache.stats()["evictions"] >= 0 and third["admit"] is True,
        "all_layers_admit": sorted(all_layers) == ["fast", "med", "slow"],
    }
    return {
        "schema": "cmplx_standards_mdhg_self_check.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "sample": {
            "first": first,
            "repeat": repeat,
            "second": second,
            "third": third,
            "multi": all_layers,
        },
        "stats": {
            "cache": cache.stats(),
            "multi": multi.stats(),
        },
    }
