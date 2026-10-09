# Conformance and Certification

## Conformance layers

1. **Record conformance:** schema, identity, source, semantic, AST, R12, MCRT, validation, and optimization fields are present.
2. **Surface conformance:** source envelopes and kernel declarations parse under the versioned grammar.
3. **Semantic conformance:** types, shapes, effects, capabilities, policy, bounds, races, and deterministic obligations are correctly classified.
4. **Lowering conformance:** accepted kernels produce equivalent backend IR with stable evidence; rejected kernels produce no artifact.
5. **Runtime conformance:** an approved artifact executes only within the declared device, memory, numerical, and sandbox profiles.
6. **Replay conformance:** hashes, diagnostics, identity, state, confidence, and outcomes can be compared across runs.

## Minimum certification set

A certification candidate should execute the entire 10,000-record corpus, not only the 1,000-script teaching pack. It must match expected accept/reject status and diagnostic codes, and produce auditable evidence for accepted programs. Any mismatch is reported by record ID and compiler/runtime version.

## Current release status

This package is structurally conformant to its own publication contract. Native language conformance remains untested because no DeepML Kernel compiler/runtime binary was supplied.
