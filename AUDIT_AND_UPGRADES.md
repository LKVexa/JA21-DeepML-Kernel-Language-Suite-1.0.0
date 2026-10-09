# JA21 DeepML Kernel Language Suite 1 0 0 main Updated Corpus Audit

This updated copy supplies device kernels, memory spaces, bounds, race and precision contracts. Its import boundary is: Rederive device metadata through a native frontend and require verified target authority and execution evidence.

## Source and coverage

Original input: `JA21-DeepML-Kernel-Language-Suite-1.0.0-main.zip`. Source SHA 256: `a6e7b0e2418e4dbc7ca66514f5df8e83a16935aff02ce4a0a3f557db8f3ff1c1`. The source archive is preserved in the parent folder. All 1,042 original leaf files were read and hashed; 21,008 stored JSONL rows were structurally parsed, including historical/reconstructed copies. Nested ZIPs are materialized in `.expanded` directories. Dataset row counts include duplicate representations and metadata headers; they are not unique executable programs.

Original checks and locations are in [the source manifest](audit/source_manifest.json). Current payload bytes are in [the updated manifest](audit/updated_manifest.json), and changes are in [the ledger](audit/change_ledger.json). Embedded source layers have [separate coverage](audit/embedded_layer_coverage.json). Historical hashes and modeled labels retain their historical meaning. The updated manifest and qualification sidecars govern this release.

## Upgrades and open implementation work

### deepml.kernel-GRAMMAR-001 High priority

Published EBNF is not complete. Undefined domain/lexical references prevent complete source parsing.

Status: **qualified; full domain grammar remains implementation backlog**. Precise per-profile grammar errata, machine-readable reference-gap index, draft lexical appendix and README link. Existing source grammar remains historical/provisional rather than being filled with permissive catch-all rules.

Evidence: `JA21-DeepML-Kernel-Language-Suite-1.0.0-main.zip::JA21-DeepML-Kernel-Language-Suite-1.0.0-main/JA21_DMK_Suite_1.0.0.zip::JA21_DMK_Suite_1.0.0/specifications/DEEPML_KERNEL_LANGUAGE.ebnf`.

Remaining gate: Full domain grammar remains open.

### deepml.kernel-EVIDENCE-001 High priority

Generated pass/runtime/AST labels are expected modeled evidence; no native compiler/runtime binary is supplied.

Status: **applied**. Every current published corpus/technical gzip record gains explicit _deepml_audit: modeled_not_executed, observed_result null, native_execution_eligible false, exact source SHA evidence and conflict quarantine.

Evidence: `JA21-DeepML-Kernel-Language-Suite-1.0.0-main.zip::JA21-DeepML-Kernel-Language-Suite-1.0.0-main/JA21_DMK_Suite_1.0.0.zip::JA21_DMK_Suite_1.0.0/corpus/technical/JA21_DMK_TECHNICAL_CORPUS_10000.jsonl.gz`.

### deepml.kernel-VALIDATOR-001 Medium priority

Inherited structural validator does not apply the published JSON Schema or demonstrate lexical, type, proof or runtime conformance.

Status: **applied and independently verified: Draft202012 full dataset validation and focused authority/corruption tests PASS**. New offline Draft202012 schema validator additionally enforces source/profile/policy consistency, independently recomputes audit qualification and checks master/shard equality. Publication schema requires the new audit extension; tests exercise source corruption, policy removal, forged execution flags and external references.

Evidence: `JA21-DeepML-Kernel-Language-Suite-1.0.0-main.zip::JA21-DeepML-Kernel-Language-Suite-1.0.0-main/JA21_DMK_Suite_1.0.0.zip::JA21_DMK_Suite_1.0.0/tools/validate_suite.py`.

### deepml.kernel-DEVICE-001 High priority

DMK-00001 source target gpu disagrees with reported device.npu effects and device.cpu capabilities. Across the master, 5231 records have at least one source-target conflict, including 3930 expected pass records and 1301 expected-failure records.

Status: **applied**. Preserve all original fields and expected outcomes; record exact warning paths/devices, quarantine conflicting metadata and deny native execution eligibility. No target is guessed.

Evidence: `JA21-DeepML-Kernel-Language-Suite-1.0.0-main.zip::JA21-DeepML-Kernel-Language-Suite-1.0.0-main/JA21_DMK_Suite_1.0.0.zip::JA21_DMK_Suite_1.0.0/corpus/technical/JA21_DMK_TECHNICAL_CORPUS_10000.jsonl.gz#DMK-00001`.

### deepml.kernel-UNIKERNEL-001 Implementation_backlog priority

Tensor/device kernels do not implement operating-system unikernel boot, image, linker, ABI, syscall/driver, memory isolation or lifecycle contracts.

Status: **design initiation prerequisite recorded**. Per-profile fabric readiness errata makes the distinction explicit and specifies a separate image/runtime contract milestone.

Evidence: `JA21-DeepML-Kernel-Language-Suite-1.0.0-main.zip::JA21-DeepML-Kernel-Language-Suite-1.0.0-main/JA21_DMK_Suite_1.0.0.zip::JA21_DMK_Suite_1.0.0/specifications/LANGUAGE_SPECIFICATION.md`.

### BASE-04 Medium priority

Nested packaging, raw modeled labels and historical copies need explicit current provenance and reuse boundaries.

Status: **APPLIED**. Expanded materialized payload; source and updated manifests; change ledger; dataset-bound qualification; individual audit and fabric role.

Evidence: `audit/source_manifest.json | audit/updated_manifest.json | audit/dataset_qualification.json`.

Remaining gate: Rederive device metadata through a native frontend and require verified target authority and execution evidence.

## Contribution to the new fabric language

Profile owner: `deepml.kernel`. Device kernels, memory spaces, bounds, race and precision contracts. Rederive device metadata through a native frontend and require verified target authority and execution evidence.

The [adapter contract](audit/fabric_adapter_contract.json) is a proposed interface with executable_adapter_implemented=false. It preserves source authority rather than using a feature label as inferred semantics. See [the collection architecture](../../fabric_language/ARCHITECTURE.md) and the [8S foundation](../../fabric_language/profiles/coupling8s/PROFILE.md).

## Qualification and verification

Use [dataset qualifications](audit/dataset_qualification.json) before training, importing or treating a record as evidence. A modeled pass or a structural validator pass is not native execution, authenticated federation, race proof, or physical device evidence. Current JA and DeepML technical records carry additional qualifications; deliberate negative examples remain negative examples.

The release provides an offline integrity checker: run `python tools/verify_release.py --deep` from the collection root. Per-profile test reports and validators qualify the exact behavior they checked. Complete grammars, native adapters, authenticated transports and a bootable unikernel remain separately tracked implementation gates.
