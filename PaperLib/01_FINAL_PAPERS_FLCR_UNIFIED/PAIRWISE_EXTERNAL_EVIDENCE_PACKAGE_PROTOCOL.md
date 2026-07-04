# Pairwise External Evidence Package Protocol

Turn every new local discovery into a paired package: internal artifact plus current peer-reviewed external paper, correlation statement, adapted validation/NIST review, crystal faces, paper routes, and obligations.

## Rule

When a new internal source, code artifact, receipt, crystal, or paper-relevant finding is discovered, search for 2025 or current-year peer-reviewed papers that constrain, support, falsify, or translate it. The pair becomes the review unit.

## Outputs

- `internal_source_card`
- `external_journal_paper_card`
- `correlation_claim`
- `claim_lane`
- `adapted_nist_pair_review`
- `validation_pair_review`
- `crystal_faces`
- `paper_routes`
- `obligations`
- `falsifier_or_comparator`

## Adapted NIST Checks

- `source_identity`
- `external_peer_review_status`
- `date_window_2025_or_current_year`
- `correlation_specificity`
- `claim_lane_declared`
- `paper_routes_declared`
- `obligations_declared`
- `falsifier_or_comparator_declared`
- `no_silent_physics_promotion`

## Date Policy

- `prefer_2025`: Require peer-reviewed journal article with year >= 2025 (default for new promotions).
- `any_peer_reviewed`: Require peer-reviewed journal article only; any publication year allowed (FLCR-24 widened hunt).

## Routing Rule

A package routes to papers 1-40 when it defines method vocabulary, proof form, memory, forge behavior, or receipt logic; it routes to papers 41-80 when it translates or constrains Standard Model or physical-domain claims.
