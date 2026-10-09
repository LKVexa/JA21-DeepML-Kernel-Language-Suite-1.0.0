# DeepML Kernel Language Suite Governance Charter

## Purpose

This charter keeps the `.dmk` suite coherent as its grammar, compiler, runtime, examples, and curriculum evolve. A release is admissible only when source semantics, policy decisions, provenance identities, and expected diagnostics remain traceable.

## Governing principles

1. **Determinism is declared, not presumed.** Every executable example identifies its determinism and precision expectations.
2. **Optimization is subordinate to equivalence.** Tiling, fusion, vectorization, device specialization, and memory transformations must preserve declared semantics within an explicit tolerance profile.
3. **Capabilities and effects remain visible.** A lowering pass may not erase a required capability check or policy decision.
4. **Negative examples are first-class assets.** Rejected programs teach the contract and must retain their expected diagnostic codes.
5. **Provenance survives folding.** R12 and MCRT identity, causal links, hashes, error state, and confidence must remain replayable.
6. **Offline is the baseline.** Hidden network execution is prohibited; network use requires an explicit future profile.
7. **Claims remain bounded.** Modeled outcomes are not reported as native compiler or runtime execution.

## Change gates

A grammar or runtime change must include: a versioned specification edit, corpus migration note, conformance cases, regenerated catalogs, script-pack impact report, and a new validation report. Breaking changes require a major version.

## Editorial roles

- **SOPHIA:** semantic review and claim boundaries
- **CHARLOTTE:** architecture and corpus release management
- **LANDON:** executable examples and diagnostics
- **Professor:** pedagogy and assessment
- **Podium:** publication quality and navigability
