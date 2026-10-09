# DeepML audit upgrades â€” 2026-10-09

Profile: `deepml.kernel` source version `0.3`. This is an upgraded publication copy. Original archives and historical reconstructions are preserved separately.

## Concrete grammar errata

The starter assert kernel.race_free == true cannot parse because primary excludes qualified_name and boolean. barrier_stmt and atomic_stmt are undefined. program allows exactly one import and policy although the prose allows one or more. Blank lines/indentation have no declared handling. Source target and repeated device metadata disagree in thousands of records; precise conflicts are quarantined in each _deepml_audit.warnings list. DeepML Kernel describes tensor/device kernels; it does not supply an operating-system unikernel boot image, linker, platform ABI or isolation runtime.

Undefined referenced productions in `specifications/DEEPML_KERNEL_LANGUAGE.ebnf`: `atomic_stmt`, `barrier_stmt`.

The grammar gaps are machine-readable in [grammar_gaps.json](grammar_gaps.json). [LEXICAL_COMPLETION_DRAFT.ebnf](LEXICAL_COMPLETION_DRAFT.ebnf) supplies candidate basic lexical definitions only; it does not turn the inherited EBNF into a parser. The editorial `couplingMechanics8SRecord` extension, when present, is disconnected from the `program` rule and requires a separate adopted extension grammar and mathematical evidence.

## Applied record qualification

Every published `corpus/technical/*.jsonl.gz` record now contains `_deepml_audit`. Legacy expected labels, source programs, source hashes, AST/R12/MCRT and provenance remain intact. An expected `pass` is an expectation: `execution_state` is `modeled_not_executed`, `observed_result` is null and `native_execution_eligible` is false. Metadata device conflicts are recorded precisely and quarantined. They are not corrected by guessing which device was intended.

[qualification_summary.json](qualification_summary.json) reports counts and representative conflicts. The published corpus schema now requires and constrains the qualification extension. Historical/reconstructed copies retain their original schema and are not upgraded execution evidence.

## Improved offline verification

Install the dependency from an approved local wheel or environment using `requirements.txt`, then run `python upgrades_deepml/validate_upgraded.py --report upgrades_deepml/UPGRADE_VALIDATION.json`. Run `python upgrades_deepml/test_qualification.py` for corruption and authority tests.

The verifier uses JSON Schema Draft 2020-12 with local references only, recomputes exact source hashes, checks the profile and standalone policy, independently recomputes device-conflict quarantine and verifies master/shard equality. It never executes the language, shaders, device operations, proofs, domain adapters or external programs. A passing result covers these structural/evidence checks only. The inherited validator remains a publication-era structural tool; its old manifests may describe pre-upgrade bytes.

## Contribution to the proposed fabric

Use Kernel for device-operation and proof-obligation columns. Keep conflicting targets quarantined, preserve all evidence, and require backend-specific bounds/race/precision proofs. Create a separate unikernel image contract for boot, memory, syscalls, network drivers, capability admission and shutdown.

Keep certification holdouts separate from training/tuning. Generated summary ASTs, claimed proofs, expected output hashes and Smithson 8S annotations require independently produced native evidence before they can authorize fabric execution.

## Completed verification

Full published-dataset Draft 2020-12 validation PASS with jsonschema 4.25.1; all six focused corruption/authority tests PASS. [UPGRADE_VALIDATION.json](UPGRADE_VALIDATION.json), [TEST_RESULTS.txt](TEST_RESULTS.txt) and [SOURCE_RECORD_PRESERVATION.json](SOURCE_RECORD_PRESERVATION.json) record the evidence. Every legacy record field was compared with the original publication and preserved exactly; only the audit extension was added. Native compilation, proof checking and runtime execution remain untested.
