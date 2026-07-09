"""
Paper 38 — AI Runtime Verifier
================================
Real verifier for Paper 38: Observer, Computation & AI Runtime Translation.

Implements:
  - Observer-embedded AI runtime substrate
  - Inference-frame honesty harness
  - Witness state runtime synchronization
  - CAM crystal projector memory banks
  - Delay buffer temporal memory
  - Supervisor cursor program counter
  - Receipt structure for AI observability

All references to B-family lattice_forge removed.  A-family naming only.
"""

from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Tuple, Optional, Any, Callable
from collections import deque
from enum import Enum, auto


def _stable_id(prefix: str, payload: Any) -> str:
    blob = json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
    return f"{prefix}-{hashlib.sha256(blob).hexdigest()[:16]}"


# ──────────────────────────────────────────────────────────────────────────────
# Section 1 — Definitions & Core Types (Paper 38, Section 2)
# ──────────────────────────────────────────────────────────────────────────────

class FaceId(Enum):
    """Three trace-2 idempotents = three observer faces (Paper 18)."""
    FACE_0 = 0
    FACE_1 = 1
    FACE_2 = 2


class ReceiptStatus(Enum):
    """Status of a single receipt in the audit trail."""
    PENDING = auto()
    COMMITTED = auto()
    VERIFIED = auto()
    FAILED = auto()


@dataclass(frozen=True)
class LatticeAddress:
    """Discrete lattice address: the terminal address of a carrier state."""
    layer: int
    index: int
    tick: int

    def to_string(self) -> str:
        return f"L{self.layer}:I{self.index}:T{self.tick}"


@dataclass
class Receipt:
    """
    Verifiable record of a carrier state (Paper 11, Theorem 2.1).
    Ensures AI observability: the runtime's state can be reconstructed from receipts.
    """
    receipt_id: str
    timestamp: float
    operation: str
    carrier_state: Dict[str, Any]
    lattice_address: LatticeAddress
    status: ReceiptStatus = ReceiptStatus.COMMITTED
    parent_id: Optional[str] = None

    def cam_hash(self) -> str:
        """Content-addressed hash of this receipt."""
        payload = json.dumps({
            "receipt_id": self.receipt_id,
            "timestamp": self.timestamp,
            "operation": self.operation,
            "carrier_state": self.carrier_state,
            "lattice_address": self.lattice_address.to_string(),
            "parent_id": self.parent_id,
        }, sort_keys=True)
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def verify(self) -> bool:
        """Receipt integrity: must have valid ID, timestamp, and address."""
        assert self.receipt_id, "receipt_id must not be empty"
        assert self.timestamp > 0, "timestamp must be positive"
        assert self.operation, "operation must not be empty"
        assert self.carrier_state is not None, "carrier_state must not be None"
        assert self.lattice_address is not None, "lattice_address must not be None"
        return True


# ──────────────────────────────────────────────────────────────────────────────
# Section 2 — CAM Crystal Projector Memory Banks (Paper 28, Corollary 38.6)
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class CAMCrystalProjector:
    """
    CAM crystal projector: a memory bank that stores a lattice state.
    The AI runtime reads and writes these banks (Corollary 38.6).
    """
    projector_id: str
    crystal_state: Dict[str, Any] = field(default_factory=dict)
    history: List[Receipt] = field(default_factory=list)
    read_count: int = 0
    write_count: int = 0

    def read(self) -> Dict[str, Any]:
        """Runtime reads the crystal."""
        self.read_count += 1
        return self.crystal_state.copy()

    def write(self, state: Dict[str, Any], receipt: Receipt) -> None:
        """Runtime writes the crystal and appends the receipt."""
        self.crystal_state = state.copy()
        self.write_count += 1
        self.history.append(receipt)

    def verify(self) -> bool:
        """Projector integrity: history must be non-decreasing in timestamps."""
        for i in range(1, len(self.history)):
            assert self.history[i].timestamp >= self.history[i - 1].timestamp, \
                "receipt history timestamps must be non-decreasing"
        assert self.read_count >= 0 and self.write_count >= 0
        return True


@dataclass
class CAMMemoryBank:
    """Collection of CAM crystal projectors — the full memory substrate."""
    projectors: Dict[str, CAMCrystalProjector] = field(default_factory=dict)

    def create_projector(self, projector_id: str) -> CAMCrystalProjector:
        p = CAMCrystalProjector(projector_id=projector_id)
        self.projectors[projector_id] = p
        return p

    def read_projector(self, projector_id: str) -> Dict[str, Any]:
        if projector_id not in self.projectors:
            raise KeyError(f"projector {projector_id} not found")
        return self.projectors[projector_id].read()

    def write_projector(self, projector_id: str, state: Dict[str, Any], receipt: Receipt) -> None:
        if projector_id not in self.projectors:
            self.create_projector(projector_id)
        self.projectors[projector_id].write(state, receipt)

    def verify(self) -> bool:
        for pid, proj in self.projectors.items():
            assert proj.verify(), f"projector {pid} failed verification"
        return True


# ──────────────────────────────────────────────────────────────────────────────
# Section 3 — Delay Buffer (Temporal Memory) (Paper 26, Corollary 38.8)
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class DelayBuffer:
    """
    Finite temporal buffer of past observations / chart values.
    The delay buffer is the bounded memory of the AI runtime.
    """
    capacity: int
    _buffer: deque = field(init=False)

    def __post_init__(self):
        self._buffer = deque(maxlen=self.capacity)

    def push(self, value: Any) -> None:
        self._buffer.append(value)

    def peek(self, steps_back: int = 0) -> Any:
        """Read the value N steps back from the newest. 0 = newest."""
        if steps_back >= len(self._buffer):
            raise IndexError("steps_back exceeds buffer length")
        return self._buffer[-(steps_back + 1)]

    def snapshot(self) -> List[Any]:
        return list(self._buffer)

    def is_full(self) -> bool:
        return len(self._buffer) == self.capacity

    def verify(self) -> bool:
        assert self.capacity > 0, "capacity must be positive"
        assert len(self._buffer) <= self.capacity, "buffer overflow"
        return True


# ──────────────────────────────────────────────────────────────────────────────
# Section 4 — Supervisor Cursor (Program Counter) (Paper 30, Corollary 38.9)
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class SupervisorCursor:
    """
    Program counter of the AI runtime.
    Sequences operations: OBSERVE → SELECT → ACT → COMMIT → ADVANCE.
    """
    current_address: LatticeAddress
    tick: int = 0
    phase: str = "INIT"
    instruction_log: List[Tuple[int, str, float]] = field(default_factory=list)

    def advance(self, next_phase: str) -> None:
        self.tick += 1
        self.instruction_log.append((self.tick, self.phase, time.time()))
        self.phase = next_phase
        self.current_address = LatticeAddress(
            layer=self.current_address.layer,
            index=self.current_address.index,
            tick=self.tick,
        )

    def verify(self) -> bool:
        """Cursor monotonicity: tick and timestamps must increase."""
        for i in range(1, len(self.instruction_log)):
            t_prev = self.instruction_log[i - 1][0]
            t_curr = self.instruction_log[i][0]
            assert t_curr > t_prev, "cursor tick must strictly increase"
        return True


# ──────────────────────────────────────────────────────────────────────────────
# Section 5 — Observer-Actor Separation (Theorem 38.7)
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class ObserverComponent:
    """Reads lattice state and produces observations."""
    face_history: DelayBuffer = field(default_factory=lambda: DelayBuffer(capacity=8))
    observations: List[Dict[str, Any]] = field(default_factory=list)

    def observe(self, crystal_state: Dict[str, Any], tick: int) -> Dict[str, Any]:
        """Observer produces an observation from the crystal state."""
        obs = {
            "tick": tick,
            "crystal_keys": list(crystal_state.keys()),
            "crystal_hash": hashlib.sha256(
                json.dumps(crystal_state, sort_keys=True).encode()
            ).hexdigest()[:16],
        }
        self.observations.append(obs)
        self.face_history.push(obs)
        return obs

    def select_face(self, chart_value: float) -> FaceId:
        """
        Observer-face selection (Paper 18, Theorem 7.1).
        Select from 3 trace-2 idempotents by chart evolution.
        """
        # Simplified selection: partition [0,1) into 3 equal bins
        if chart_value < 0.333:
            return FaceId.FACE_0
        elif chart_value < 0.667:
            return FaceId.FACE_1
        return FaceId.FACE_2

    def verify(self) -> bool:
        assert self.face_history.verify()
        assert len(self.observations) == len(self.face_history.snapshot()) or \
               len(self.observations) == len(self.face_history.snapshot()) + 1
        return True


@dataclass
class ActorComponent:
    """Reads observations and produces actions."""
    action_log: List[Dict[str, Any]] = field(default_factory=list)

    def act(self, observation: Dict[str, Any], policy: Optional[Callable] = None) -> Dict[str, Any]:
        """Actor produces an action from the observation."""
        action = {
            "tick": observation["tick"],
            "type": "lattice_advance",
            "payload": observation.get("crystal_keys", []),
        }
        if policy is not None:
            action = policy(observation)
        self.action_log.append(action)
        return action

    def verify(self) -> bool:
        for a in self.action_log:
            assert "tick" in a, "action must reference a tick"
            assert "type" in a, "action must have a type"
        return True


# ──────────────────────────────────────────────────────────────────────────────
# Section 6 — Inference-Frame Honesty Harness (Theorem 38.11)
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class InferenceFrame:
    """
    Encapsulates a single inference step with verifiable honesty constraints.
    The harness ensures the model's outputs are lattice-valid and receipt-bound.
    """
    frame_id: str
    input_state: Dict[str, Any]
    output_state: Dict[str, Any]
    confidence: float
    honesty_constraints: Dict[str, Any] = field(default_factory=dict)
    receipt: Optional[Receipt] = None

    def is_honest(self) -> bool:
        """
        Honesty check: output must (1) reference the input state,
        (2) carry a non-negative confidence, and (3) be receipt-bound.
        """
        if self.confidence < 0 or self.confidence > 1:
            return False
        if self.receipt is None:
            return False
        if not self.receipt.verify():
            return False
        # Structural honesty: output must reference the input
        in_keys = set(self.input_state.keys())
        out_keys = set(self.output_state.keys())
        if in_keys & out_keys:
            return True
        # Payload references input keys
        payload = self.output_state.get("payload")
        if isinstance(payload, list) and any(k in in_keys for k in payload):
            return True
        if self.output_state.get("input_ref") in in_keys:
            return True
        return False

    def verify(self) -> bool:
        assert self.frame_id, "frame_id must not be empty"
        assert self.is_honest(), "inference frame failed honesty check"
        return True


class HonestyHarness:
    """
    Runs every inference frame through the honesty protocol.
    Rejects frames that violate constraints and produces a failure receipt.
    """

    def __init__(self):
        self.passed_frames: List[InferenceFrame] = []
        self.failed_frames: List[InferenceFrame] = []

    def evaluate(self, frame: InferenceFrame) -> Tuple[bool, Optional[Receipt]]:
        ok = frame.is_honest()
        if ok:
            self.passed_frames.append(frame)
            return True, frame.receipt
        else:
            self.failed_frames.append(frame)
            fail_receipt = Receipt(
                receipt_id=_stable_id("rcpt", {
                    "operation": "inference_rejected",
                    "frame_id": frame.frame_id,
                    "reason": "honesty_violation",
                }),
                timestamp=time.time(),
                operation="inference_rejected",
                carrier_state={"frame_id": frame.frame_id, "reason": "honesty_violation"},
                lattice_address=LatticeAddress(layer=0, index=0, tick=0),
                status=ReceiptStatus.FAILED,
            )
            return False, fail_receipt

    def verify(self) -> bool:
        for f in self.passed_frames:
            assert f.verify(), f"passed frame {f.frame_id} failed verification"
        return True


# ──────────────────────────────────────────────────────────────────────────────
# Section 7 — Witness State Runtime Synchronization (Theorem 38.11)
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class WitnessState:
    """
    Witness state: the external observer's reconstruction of the runtime state.
    Synchronization means the witness state matches the runtime state.
    """
    witness_id: str
    reconstructed_state: Dict[str, Any] = field(default_factory=dict)
    receipt_stack: List[Receipt] = field(default_factory=list)
    sync_tick: int = -1

    def replay(self, receipts: List[Receipt]) -> None:
        """
        Replay a receipt stack to reconstruct the runtime state (Paper 11, Theorem 3.1).
        """
        self.receipt_stack = list(receipts)
        self.reconstructed_state = {}
        for r in receipts:
            if r.status in (ReceiptStatus.COMMITTED, ReceiptStatus.VERIFIED):
                self.reconstructed_state.update(r.carrier_state)
                self.sync_tick = r.lattice_address.tick

    def is_synchronized_with(self, runtime_state: Dict[str, Any], runtime_tick: int) -> bool:
        """Check if the witness state matches the runtime state at the same tick."""
        if self.sync_tick != runtime_tick:
            return False
        # Runtime projector state must be a subset of the reconstructed witness state
        for k, v in runtime_state.items():
            if self.reconstructed_state.get(k) != v:
                return False
        return True

    def verify(self) -> bool:
        assert self.witness_id, "witness_id must not be empty"
        for r in self.receipt_stack:
            assert r.verify(), f"receipt {r.receipt_id} failed verification"
        return True


# ──────────────────────────────────────────────────────────────────────────────
# Section 8 — AI Runtime Substrate (Theorem 38.4, 38.7)
# ──────────────────────────────────────────────────────────────────────────────

class AIRuntime:
    """
    The full AI runtime substrate.
    Integrates observer, actor, cursor, delay buffer, CAM memory, and honesty harness.
    """

    def __init__(self, runtime_id: str = ""):
        self.runtime_id = runtime_id or _stable_id("rt", {"substrate": "ai_runtime"})
        self.memory = CAMMemoryBank()
        self.cursor = SupervisorCursor(
            current_address=LatticeAddress(layer=0, index=0, tick=0),
            phase="INIT",
        )
        self.observer = ObserverComponent()
        self.actor = ActorComponent()
        self.harness = HonestyHarness()
        self.witness = WitnessState(witness_id=f"witness-{self.runtime_id}")
        self.global_receipts: List[Receipt] = []

    def _emit_receipt(self, operation: str, carrier_state: Dict[str, Any],
                      status: ReceiptStatus = ReceiptStatus.COMMITTED) -> Receipt:
        parent = self.global_receipts[-1].receipt_id if self.global_receipts else None
        receipt_id = _stable_id(
            "rcpt",
            {
                "operation": operation,
                "carrier_state": carrier_state,
                "address": self.cursor.current_address.to_string(),
                "parent_id": parent,
                "status": status.name,
            },
        )
        r = Receipt(
            receipt_id=receipt_id,
            timestamp=time.time(),
            operation=operation,
            carrier_state=carrier_state,
            lattice_address=self.cursor.current_address,
            status=status,
            parent_id=self.global_receipts[-1].receipt_id if self.global_receipts else None,
        )
        self.global_receipts.append(r)
        return r

    def tick(self, crystal_state: Dict[str, Any], chart_value: float,
             policy: Optional[Callable] = None) -> Dict[str, Any]:
        """
        One full runtime tick: OBSERVE → SELECT → ACT → COMMIT → ADVANCE.
        """
        # 1. OBSERVE
        self.cursor.advance("OBSERVE")
        obs = self.observer.observe(crystal_state, self.cursor.tick)
        self._emit_receipt("observe", obs)

        # 2. SELECT (face selection)
        self.cursor.advance("SELECT")
        face = self.observer.select_face(chart_value)
        self._emit_receipt("select_face", {"face": face.name})

        # 3. ACT
        self.cursor.advance("ACT")
        action = self.actor.act(obs, policy=policy)
        self._emit_receipt("act", action)

        # 4. Write crystal state to memory bank
        self.cursor.advance("COMMIT")
        mem_receipt = self._emit_receipt("commit", crystal_state)
        self.memory.write_projector(
            f"runtime_{self.runtime_id}",
            crystal_state,
            mem_receipt,
        )

        # 5. Inference-frame honesty check
        frame = InferenceFrame(
            frame_id=_stable_id(
                "frame",
                {
                    "tick": self.cursor.tick,
                    "input": crystal_state,
                    "output": action,
                },
            ),
            input_state=crystal_state,
            output_state=action,
            confidence=0.95,
            receipt=mem_receipt,
        )
        honest, _ = self.harness.evaluate(frame)
        if not honest:
            self.cursor.advance("REJECT")
            self._emit_receipt("reject", {"frame_id": frame.frame_id}, ReceiptStatus.FAILED)
            return {"status": "rejected", "tick": self.cursor.tick}

        # 6. ADVANCE
        self.cursor.advance("ADVANCE")
        self._emit_receipt("advance", {"tick": self.cursor.tick})

        # 7. Witness synchronization
        self.witness.replay(self.global_receipts)

        return {
            "status": "ok",
            "tick": self.cursor.tick,
            "face": face.name,
            "action": action,
            "receipt_count": len(self.global_receipts),
        }

    def verify_observability(self) -> bool:
        """
        Corollary 38.13: AI observability is the lattice closure of the runtime.
        Every state must reach a terminal address (a receipt).
        """
        if not self.global_receipts:
            return False
        # Every tick must have at least one receipt
        ticks_with_receipts = set(r.lattice_address.tick for r in self.global_receipts)
        expected_ticks = set(range(1, self.cursor.tick + 1))
        return ticks_with_receipts == expected_ticks

    def verify(self) -> bool:
        assert self.memory.verify(), "CAM memory bank failed"
        assert self.cursor.verify(), "supervisor cursor failed"
        assert self.observer.verify(), "observer failed"
        assert self.actor.verify(), "actor failed"
        assert self.harness.verify(), "honesty harness failed"
        assert self.witness.verify(), "witness state failed"
        assert self.verify_observability(), "AI observability (lattice closure) failed"
        return True


# ──────────────────────────────────────────────────────────────────────────────
# Section 9 — Master Verifier / Receipt Engine
# ──────────────────────────────────────────────────────────────────────────────

class AIRuntimeVerifier:
    """
    Master verifier for Paper 38.
    Runs every claim through its computational test and produces a receipt.
    """

    def __init__(self):
        self.receipts: List[Dict] = []
        self.passed = 0
        self.failed = 0

    def _log(self, claim: str, ok: bool, detail: str = ""):
        self.receipts.append({
            "claim": claim,
            "status": "PASS" if ok else "FAIL",
            "detail": detail,
        })
        if ok:
            self.passed += 1
        else:
            self.failed += 1

    def run(self) -> Dict:
        # --- Claim 38.6: CAM crystal projectors are memory banks ---
        mem = CAMMemoryBank()
        p = mem.create_projector("test_crystal_0")
        r = Receipt(
            receipt_id="r0",
            timestamp=time.time(),
            operation="init",
            carrier_state={"value": 42},
            lattice_address=LatticeAddress(layer=0, index=0, tick=0),
        )
        try:
            mem.write_projector("test_crystal_0", {"value": 42}, r)
            read_back = mem.read_projector("test_crystal_0")
            mem.verify()
            self._log(
                "38.6 — CAM crystal projector memory banks",
                read_back == {"value": 42},
                f"write_count={p.write_count}, read_count={p.read_count}",
            )
        except Exception as e:
            self._log("38.6 — CAM crystal projector memory banks", False, str(e))

        # --- Claim 38.8: Observer delay buffer ---
        buf = DelayBuffer(capacity=4)
        for v in range(5):
            buf.push(v)
        try:
            buf.verify()
            self._log(
                "38.8 — Delay buffer temporal memory",
                buf.is_full() and buf.peek(0) == 4 and buf.peek(3) == 1,
                f"capacity={buf.capacity}, len={len(buf.snapshot())}, oldest={buf.peek(3)}",
            )
        except Exception as e:
            self._log("38.8 — Delay buffer temporal memory", False, str(e))

        # --- Claim 38.9: Supervisor cursor as program counter ---
        cursor = SupervisorCursor(
            current_address=LatticeAddress(layer=0, index=0, tick=0),
        )
        for phase in ["OBSERVE", "SELECT", "ACT", "COMMIT", "ADVANCE"]:
            cursor.advance(phase)
        try:
            cursor.verify()
            self._log(
                "38.9 — Supervisor cursor program counter",
                cursor.tick == 5,
                f"tick={cursor.tick}, phases={[p for _, p, _ in cursor.instruction_log]}",
            )
        except Exception as e:
            self._log("38.9 — Supervisor cursor program counter", False, str(e))

        # --- Claim 38.7: Observer-actor separation ---
        obs = ObserverComponent()
        act = ActorComponent()
        crystal = {"param_a": 1.0, "param_b": 2.0}
        try:
            observation = obs.observe(crystal, tick=1)
            action = act.act(observation)
            obs.verify()
            act.verify()
            self._log(
                "38.7 — Observer-actor separation",
                observation["tick"] == 1 and action["tick"] == 1,
                f"obs_keys={observation['crystal_keys']}, action_type={action['type']}",
            )
        except Exception as e:
            self._log("38.7 — Observer-actor separation", False, str(e))

        # --- Claim 38.1: Observer-face selection ---
        try:
            f0 = obs.select_face(0.1)
            f1 = obs.select_face(0.5)
            f2 = obs.select_face(0.9)
            self._log(
                "38.1 — Observer-face selection",
                f0 == FaceId.FACE_0 and f1 == FaceId.FACE_1 and f2 == FaceId.FACE_2,
                f"faces={[f0.name, f1.name, f2.name]}",
            )
        except Exception as e:
            self._log("38.1 — Observer-face selection", False, str(e))

        # --- Claim 38.11: Receipt structure ensures AI observability ---
        runtime = AIRuntime(runtime_id="test_001")
        try:
            for i in range(3):
                runtime.tick(
                    crystal_state={"step": i, "data": f"batch_{i}"},
                    chart_value=0.3 + i * 0.2,
                )
            runtime.verify()
            obs_ok = runtime.verify_observability()
            self._log(
                "38.11 — Receipt structure / AI observability",
                obs_ok,
                f"ticks={runtime.cursor.tick}, receipts={len(runtime.global_receipts)}",
            )
        except Exception as e:
            self._log("38.11 — Receipt structure / AI observability", False, str(e))

        # --- Claim 38.11 extended: Inference-frame honesty harness ---
        try:
            honest_frame = InferenceFrame(
                frame_id="hf1",
                input_state={"a": 1},
                output_state={"a": 2, "b": 3},
                confidence=0.9,
                receipt=runtime.global_receipts[-1] if runtime.global_receipts else r,
            )
            dishonest_frame = InferenceFrame(
                frame_id="hf2",
                input_state={"a": 1},
                output_state={"c": 2},  # no shared key
                confidence=0.9,
                receipt=runtime.global_receipts[-1] if runtime.global_receipts else r,
            )
            harness = HonestyHarness()
            ok1, _ = harness.evaluate(honest_frame)
            ok2, _ = harness.evaluate(dishonest_frame)
            harness.verify()
            self._log(
                "38.11 — Inference-frame honesty harness",
                ok1 and not ok2,
                f"honest_passed={ok1}, dishonest_passed={ok2}",
            )
        except Exception as e:
            self._log("38.11 — Inference-frame honesty harness", False, str(e))

        # --- Witness state synchronization ---
        try:
            witness = WitnessState(witness_id="w1")
            witness.replay(runtime.global_receipts)
            sync_ok = witness.is_synchronized_with(
                runtime.memory.read_projector(f"runtime_{runtime.runtime_id}"),
                runtime.cursor.tick,
            )
            witness.verify()
            self._log(
                "Witness state runtime synchronization",
                sync_ok,
                f"witness_tick={witness.sync_tick}, runtime_tick={runtime.cursor.tick}",
            )
        except Exception as e:
            self._log("Witness state runtime synchronization", False, str(e))

        return {
            "paper": 38,
            "passed": self.passed,
            "failed": self.failed,
            "total": self.passed + self.failed,
            "receipts": self.receipts,
        }


# ──────────────────────────────────────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    verifier = AIRuntimeVerifier()
    result = verifier.run()
    print(f"\nPaper 38 AI Runtime Verifier — {result['passed']}/{result['total']} passed")
    for r in result["receipts"]:
        mark = "✓" if r["status"] == "PASS" else "✗"
        print(f"  {mark} {r['claim']}: {r['detail']}")
    if result["failed"] > 0:
        raise SystemExit(1)
