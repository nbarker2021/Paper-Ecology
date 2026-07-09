"""Adapter for FLCR80 repo slot readings."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any


CMPLX_ROOT = Path(__file__).resolve().parents[2]
BUILDER = CMPLX_ROOT / "tools" / "build_flcr80_repo_slot_readings.py"


def _load_builder():
    spec = importlib.util.spec_from_file_location("build_flcr80_repo_slot_readings", BUILDER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot_load_builder:{BUILDER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_flcr80_repo_slot_payload() -> dict[str, Any]:
    module = _load_builder()
    slots, _ = module.load_slots()
    module.write_slot_definition(slots)
    payload = module.build()
    module.OUT_JSON.write_text(module.json.dumps(payload, indent=2), encoding="utf-8")
    module.write_markdown(payload)
    return payload
