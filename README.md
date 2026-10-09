# JA21-DeepML-Kernel-Language-Suite-1.0.0

Explore device-kernel language design with JA21 DeepML Kernel: 10,000 technical records, 1,000 .dmk scripts, and a 20-chapter textbook. Study memory spaces, bounds, race, and precision contracts through examples, diagnostics, provenance models, and offline tools. Develop your understanding of kernel contracts; native device execution is not tested.

The JA21 DeepML Kernel Language Suite provides an offline source and teaching collection for device-kernel programming concepts. Its focus includes memory spaces, bounds, race-related obligations, precision, and the evidence needed to connect a language description to a target device. It is useful for educators, students, compiler developers, and researchers designing kernel-language tooling.

The package combines 10,000 normalized technical records, 1,000 curated .dmk scripts, and a 20-chapter textbook with worked examples, laboratories, and review questions. Its 31 features are organized across ten proficiency levels and ten validation classes. Catalogs, diagnostic navigation, a starter project, curriculum, workbook, instructor guide, grammar assets, compiler/runtime contracts, and R12/MCRT provenance specifications support both independent study and structured teaching.

The audited publication checks schemas, source hashes, policies, and package consistency, and labels expected results as modeled evidence. It does not supply a native compiler or device runtime. Full parsing, target authorization, race proofs, numerical correctness, and observed device execution require further implementation and evidence. Preserved Smithson 8S annotations retain their stated scientific and execution limitations.

## Corpora and audit records

The supplied corpus layout is preserved under `payload/`. The `audit/` directory and [AUDIT_AND_UPGRADES.md](AUDIT_AND_UPGRADES.md) record source coverage, release changes, and evidence boundaries.

Historical source archives and source manifests remain provenance records. Current publication file hashes are listed in `PUBLICATION_SHA256.json`; licensing changes are recorded in `PUBLICATION_LICENSE_LEDGER.json`.

## License

JA21-DeepML-Kernel-Language-Suite-1.0.0 (C) 2026 RUSSELL PHILIP SMITHSON

Licensed under the GNU General Public License version 3 only (`GPL-3.0-only`). See [LICENSE](LICENSE) and [NOTICE](NOTICE).
