# Suite Catalog

## Primary deliverables

| Deliverable | Location | Contents |
|---|---|---|
| Technical corpus | `corpus/technical/` | 10,000 normalized JSONL records plus document metadata |
| Corpus index | `corpus/index/technical_corpus_index.csv` | Record-to-feature, source hash, semantic, AST, R12, and MCRT map |
| Script example pack | `scripts/` | 1,000 individual `.dmk` programs, stratified across every level and validation class |
| Script catalog | `catalogs/SCRIPT_CATALOG.csv` | Searchable explanation and provenance for each program |
| Textbook | `textbook/JA21_DEEPML_KERNEL_LANGUAGE_TEXTBOOK.md` | Twenty chapters, worked examples, laboratories, review questions, glossary |
| Education pack | `education/` | Twelve-week curriculum, student workbook, instructor guide |
| Language contracts | `specifications/` | Provisional EBNF, language, compiler, runtime, R12/MCRT, conformance |
| Offline tools | `tools/` | Corpus inspection and package validation |
| Evidence | `manifests/` | Machine-readable inventory and SHA-256 checksums |

## Script pack by validation class

| Validation class | Corpus | Script pack |
|---|---:|---:|
| Positive | 4,000 | 400 |
| Negative | 1,500 | 150 |
| Boundary | 1,000 | 100 |
| Integration | 1,000 | 100 |
| Security | 750 | 75 |
| Performance | 500 | 50 |
| Determinism | 500 | 50 |
| Interoperability | 250 | 25 |
| Recovery | 250 | 25 |
| Certification | 250 | 25 |

## Feature coverage

| Feature | Learning track | Corpus | Script pack |
|---|---|---:|---:|
| `atomic_operation` | Correctness & assurance | 324 | 107 |
| `autodiff_primitive` | Compiler & optimization | 323 | 19 |
| `backend_lowering` | Compiler & optimization | 322 | 35 |
| `barrier` | Correctness & assurance | 323 | 11 |
| `bounds_proof` | Correctness & assurance | 322 | 26 |
| `custom_operator` | Compiler & optimization | 323 | 6 |
| `determinism_mode` | Correctness & assurance | 322 | 6 |
| `device_target` | Device & deployment | 323 | 33 |
| `device_transfer` | Memory & movement | 323 | 43 |
| `global_memory` | Memory & movement | 322 | 35 |
| `kernel_fusion` | Compiler & optimization | 324 | 31 |
| `launch_dimensions` | Parallel execution | 323 | 40 |
| `layout` | Memory & movement | 322 | 48 |
| `local_memory` | Memory & movement | 323 | 35 |
| `memory_space` | Memory & movement | 322 | 8 |
| `parallel_loop` | Parallel execution | 322 | 24 |
| `precision_mode` | Compiler & optimization | 322 | 5 |
| `quantized_type` | Types & shapes | 322 | 27 |
| `race_analysis` | Correctness & assurance | 322 | 38 |
| `reduction` | Compiler & optimization | 322 | 34 |
| `scalar_type` | Types & shapes | 322 | 45 |
| `shared_memory` | Memory & movement | 322 | 15 |
| `simd` | Parallel execution | 324 | 35 |
| `sparse_type` | Types & shapes | 322 | 11 |
| `static_shape` | Types & shapes | 322 | 50 |
| `stride` | Memory & movement | 324 | 8 |
| `symbolic_shape` | Types & shapes | 322 | 21 |
| `tensor_type` | Types & shapes | 324 | 14 |
| `tiling` | Parallel execution | 322 | 33 |
| `tolerance_equivalence` | Correctness & assurance | 323 | 65 |
| `vectorization` | Parallel execution | 322 | 92 |

## Navigation guidance

Use the textbook when learning concepts in sequence. Use the script catalog when searching for a concrete language feature or failure mode. Use the technical corpus for compiler, evaluator, retrieval, and training workflows. Use the specifications when implementing a parser, lowering pass, runtime adapter, or conformance harness.
