# JA21 DeepML Kernel Language
## A Technical Textbook for Deterministic Tensor Kernels, Compiler Evidence, and Device Runtime Assurance

**Suite edition:** 1.0.0  
**Language profile:** `deepml.kernel`  
**Primary extension:** `.dmk`  
**Corpus scale:** 10,000 technical records  
**Example pack:** 1,000 curated scripts

---

> A kernel is not complete when it is fast. It is complete when its meaning, authority, numerical contract, transformation history, and runtime evidence remain visible.

## Preface

This book turns the uploaded DeepML Kernel corpus into a teachable language suite. It is written for language designers, compiler engineers, runtime developers, technical artists, ML-systems engineers, auditors, and advanced students. The examples are grounded in the supplied records and retain their expected validation metadata.

The book makes a strict distinction between **specified outcome** and **executed outcome**. The corpus specifies what should pass or fail, but a production compiler/runtime was not included. Exercises that ask for execution assume a future implementation or a student-built reference toolchain.

## How to use the book

- Chapters 1–4 establish syntax, types, and shapes.
- Chapters 5–9 cover parallel execution, memory, synchronization, and operators.
- Chapters 10–14 connect source to compiler, provenance, numerical, and optimization contracts.
- Chapters 15–19 cover diagnostics, security, performance, 8S annotation, and certification.
- Chapter 20 is a complete toolchain capstone.

## Contents

1. [Why a Kernel Language?](#chapter-1-why_a_kernel_language)
2. [Program Anatomy and Surface Syntax](#chapter-2-program_anatomy_and_surface_syntax)
3. [Scalar, Tensor, Quantized, and Sparse Types](#chapter-3-scalar_tensor_quantized_and_sparse_types)
4. [Static and Symbolic Shapes](#chapter-4-static_and_symbolic_shapes)
5. [Parallel Iteration and Launch Geometry](#chapter-5-parallel_iteration_and_launch_geometry)
6. [Tiling, SIMD, and Vectorization](#chapter-6-tiling_simd_and_vectorization)
7. [Memory Spaces, Layouts, and Strides](#chapter-7-memory_spaces_layouts_and_strides)
8. [Bounds, Barriers, Atomics, and Race Freedom](#chapter-8-bounds_barriers_atomics_and_race_freedom)
9. [Reductions and Custom Operators](#chapter-9-reductions_and_custom_operators)
10. [AST, Semantic Judgments, Effects, and Capabilities](#chapter-10-ast_semantic_judgments_effects_and_capabilities)
11. [Backend Lowering and Device Targets](#chapter-11-backend_lowering_and_device_targets)
12. [R12 Lowering and MCRT Provenance](#chapter-12-r12_lowering_and_mcrt_provenance)
13. [Precision, Determinism, and Tolerance Equivalence](#chapter-13-precision_determinism_and_tolerance_equivalence)
14. [Autodiff Primitives and Kernel Fusion](#chapter-14-autodiff_primitives_and_kernel_fusion)
15. [Diagnostics, Negative Tests, and Recovery](#chapter-15-diagnostics_negative_tests_and_recovery)
16. [Security, Offline Policy, and Deployment](#chapter-16-security_offline_policy_and_deployment)
17. [Performance Engineering Without Semantic Drift](#chapter-17-performance_engineering_without_semantic_drift)
18. [Smithson 8S Coupled Mechanics Profile](#chapter-18-smithson_8s_coupled_mechanics_profile)
19. [Conformance and Certification Engineering](#chapter-19-conformance_and_certification_engineering)
20. [Capstone: A Standalone Kernel Toolchain](#chapter-20-capstone_a_standalone_kernel_toolchain)

---


---

# Chapter 1: Why a Kernel Language?

## Learning objectives

- Explain why device kernels benefit from an explicit language contract
- Distinguish surface code, semantic judgment, compiler evidence, and runtime evidence
- Describe the suite’s modeled-not-executed validation boundary

DeepML Kernel Language is a compact language for expressing tensor-oriented device work while keeping operational risk visible. General-purpose languages often hide the boundary between source intent and backend behavior. A kernel language can instead make target, precision, determinism, memory, bounds verification, race safety, policy, and artifact emission part of the program itself.

The suite treats a program as more than text. Each technical record connects source to a semantic interpretation, an AST, compiler representation, runtime representation, technical explanation, expected validation outcome, optimization constraints, and coupling-mechanics annotation. This is useful for teaching, compiler testing, retrieval, conformance, and audit because a learner can follow one record through the entire stack.

The corpus does not prove that a production compiler accepted the examples. Its validation results explicitly say `modeled_not_executed`. That distinction is central: the corpus defines intended behavior; a native implementation must still demonstrate that behavior.

## Worked corpus example

**Corpus anchor:** `DMK-00280` · `beginner` · `positive`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_00280
use DeepMLKernel
policy no_network

kernel DMK_00280(input: Tensor<f32>[88,16]) -> Tensor<f32>[88,16]
target gpu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..88 tile 16 {
        vectorize 16
        output[i] = input[i] * 2.0
    }
}
verify bounds with checked
assert kernel.race_free == true
emit kernel "DMK_00280.dmk"
```

## Laboratory

Map the files for one selected record: source script, script-catalog row, technical-corpus row, R12 record, and MCRT record. Write a one-page trace of the evidence chain.

## Review questions

1. What does a kernel language expose that a host language may hide?
2. Why must modeled and executed validation be reported separately?
3. Which evidence survives from source through runtime?


---

# Chapter 2: Program Anatomy and Surface Syntax

## Learning objectives

- Read the canonical `.dmk` compilation-unit envelope
- Identify declarations that affect policy and execution
- Use the provisional EBNF as an implementation starting point

A canonical corpus program begins with a JA source version and module identity, imports `DeepMLKernel`, declares `policy no_network`, and defines one kernel. The kernel signature contains tensor types and shapes. The declarations below the signature select a target, precision mode, determinism mode, and memory space. The body expresses parallel work. Verification and assertion lines state obligations before the program names its emitted artifact.

The syntax is deliberately declarative. `target gpu` is not a performance promise; it is a backend requirement to be validated. `precision strict` constrains legal numerical transformations. `determinism reproducible` asks the compiler and runtime to preserve a reproducibility profile. `memory global` identifies the default address space. `verify bounds with checked` and `assert kernel.race_free == true` create proof obligations rather than comments.

The EBNF in this suite is provisional because the upload supplied corpus instances rather than a production parser specification. It captures the observed common language and creates a stable target for the first parser and formatter.

## Worked corpus example

**Corpus anchor:** `DMK-00635` · `beginner` · `boundary`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_00635
use DeepMLKernel
policy no_network

kernel DMK_00635(input: Tensor<f32>[55,1]) -> Tensor<f32>[55,1]
target npu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..55 tile 1 {
        vectorize 1
        output[i] = input[i] * 16.0
    }
}
verify bounds with checked
assert kernel.race_free == true
emit kernel "DMK_00635.dmk"
```

## Laboratory

Modify the starter kernel’s module, tensor dimensions, target, and arithmetic constant. Then enumerate every semantic or runtime field that should change and every identity that should remain linked.

## Review questions

1. Which declarations belong outside the kernel body?
2. Why is an assertion different from documentation?
3. What should a parser do with an unknown execution declaration?


---

# Chapter 3: Scalar, Tensor, Quantized, and Sparse Types

## Learning objectives

- Describe the core type families
- Relate element type and shape to memory and device behavior
- Identify where quantized and sparse semantics require extra contracts

A tensor type combines an element type with an ordered shape. `Tensor<f32>[3,32]` describes rank two, but it does not by itself determine physical layout, stride, alignment, or address space. Those properties belong to later declarations or compiler representations. This separation lets type checking reason about values while lowering reasons about storage.

Scalar types control range and numerical behavior. Floating-point precision influences tolerance, reassociation, vectorization, and device compatibility. Integer types influence overflow and exactness. Quantized types add scale, zero point, calibration, and dequantization obligations. Sparse types add index representation, ordering, duplicate handling, and density assumptions. A compiler must not treat either as a dense tensor with a smaller footprint unless equivalence is proven.

The corpus feature vocabulary includes `scalar_type`, `tensor_type`, `quantized_type`, and `sparse_type`. Together they give a test author four different places to ask whether a transformation preserved meaning.

## Worked corpus example

**Corpus anchor:** `DMK-00350` · `beginner` · `positive`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_00350
use DeepMLKernel
policy no_network

kernel DMK_00350(input: Tensor<f32>[61,48]) -> Tensor<f32>[61,48]
target npu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..61 tile 32 {
        vectorize 16
        output[i] = input[i] * 10.0
    }
}
verify bounds with checked
assert kernel.race_free == true
emit kernel "DMK_00350.dmk"
```

## Laboratory

Choose one dense, one quantized, and one sparse record. Draft a type-checking checklist and identify backend capabilities needed for each.

## Review questions

1. Why does a tensor type not fully define layout?
2. What metadata makes quantization meaningful?
3. Which invariants are unique to sparse storage?


---

# Chapter 4: Static and Symbolic Shapes

## Learning objectives

- Distinguish static dimensions from symbolic dimensions
- Explain shape substitution and constraint solving
- Connect shape proofs to bounds and launch dimensions

Static shapes are known during compilation and can enable aggressive specialization. Symbolic shapes remain parameters constrained by equalities, inequalities, divisibility, or backend limits. A symbolic dimension is not an excuse to skip proof: the compiler must either discharge obligations for all admissible values or generate guarded runtime checks.

Shape reasoning touches every layer. The AST records the declared shape; semantic analysis resolves compatibility; lowering chooses tiles, vector widths, and launch geometry; runtime binds actual dimensions; replay evidence records the source and execution identities. A mismatched shape may be a type error, a bounds error, a device-limit error, or a recoverable specialization request depending on the contract.

Boundary examples are especially valuable here. They exercise zero-sized domains, dimensions near tile boundaries, nonmultiples of vector width, and maximum backend limits without assuming that every edge case is invalid.

## Worked corpus example

**Corpus anchor:** `DMK-00616` · `beginner` · `boundary`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_00616
use DeepMLKernel
policy no_network

kernel DMK_00616(input: Tensor<f32>[36,1]) -> Tensor<f32>[36,1]
target gpu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..36 tile 1 {
        vectorize 1
        output[i] = input[i] * 28.0
    }
}
verify bounds with checked
assert kernel.race_free == true
emit kernel "DMK_00616.dmk"
```

## Laboratory

Create a symbolic-shape variant of a static example. Specify constraints for positive dimensions, tile compatibility, and maximum launch size. Describe compile-time and runtime enforcement.

## Review questions

1. When may a symbolic shape be specialized?
2. What is the difference between a guard and a proof?
3. Why should zero-sized kernels have a declared policy?


---

# Chapter 5: Parallel Iteration and Launch Geometry

## Learning objectives

- Read a parallel iteration domain
- Relate logical indexes to device launch dimensions
- Recognize undercoverage, overcoverage, and inactive-lane handling

A parallel loop states logical independence or a requirement to prove safe dependence. Backend launch geometry maps that logical domain onto workgroups, blocks, warps, waves, vector lanes, or NPU tiles. The source should remain portable even when the mapping changes.

Correct launch planning covers every legal logical index exactly as required. Extra physical lanes may be legal when guarded. Missing lanes are not. Duplicate execution is only legal for idempotent or explicitly reduced effects. Launch dimensions also interact with device limits, shared-memory use, register pressure, occupancy, and deterministic scheduling.

The compiler should keep logical-domain identity separate from physical launch geometry. That separation allows retargeting while retaining semantic and provenance records.

## Worked corpus example

**Corpus anchor:** `DMK-00413` · `beginner` · `negative`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_00413
use DeepMLKernel
policy no_network

kernel DMK_00413(input: Tensor<f32>[27,32]) -> Tensor<f32>[27,32]
target npu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..27 tile 32 {
        vectorize 16
        output[i] = input[i] * 11.0
    }
}
verify bounds with unchecked
assert kernel.race_free == false
emit kernel "DMK_00413.dmk"
```

## Laboratory

For three tensor shapes, design CPU, GPU, and NPU launch mappings. Show guards for incomplete tiles and list the evidence needed to prove coverage.

## Review questions

1. Why must logical and physical index spaces remain distinct?
2. When are extra launched lanes safe?
3. Which launch changes can affect determinism?


---

# Chapter 6: Tiling, SIMD, and Vectorization

## Learning objectives

- Explain tiling as locality transformation
- Distinguish SIMD hardware from source vectorization intent
- State equivalence conditions for vectorized execution

Tiling partitions a logical domain into blocks chosen for locality, synchronization, and backend limits. Vectorization groups scalar operations into lanes. SIMD describes a hardware or execution model that may implement vectorized code, but source intent and backend realization are not identical.

A legal transformation preserves domain coverage, indexing, memory aliasing, numerical order where required, exception behavior, and tail handling. Strict precision may forbid reassociation that a fast profile allows. Symbolic shapes require either a generic tail path or guarded specialization. A vector width that exceeds alignment or device capability must be rejected or lowered differently.

Performance reasoning should record why a tile or width was chosen rather than treating a number as universally optimal. The corpus’s optimization notes correctly subordinate these choices to semantic equivalence and declared numerical tolerance.

## Worked corpus example

**Corpus anchor:** `DMK-00059` · `beginner` · `positive`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_00059
use DeepMLKernel
policy no_network

kernel DMK_00059(input: Tensor<f32>[61,64]) -> Tensor<f32>[61,64]
target npu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..61 tile 32 {
        vectorize 16
        output[i] = input[i] * 29.0
    }
}
verify bounds with checked
assert kernel.race_free == true
emit kernel "DMK_00059.dmk"
```

## Laboratory

Take a scalar loop and propose tile sizes 16 and 32 with vector widths 4, 8, and 16. For each combination, list alignment, tail, register, and determinism risks.

## Review questions

1. What makes tiling semantics-preserving?
2. Why is vector width not just a performance parameter?
3. How can strict precision limit SIMD transformations?


---

# Chapter 7: Memory Spaces, Layouts, and Strides

## Learning objectives

- Identify global, shared, and local memory roles
- Explain layout and stride independently of tensor shape
- Reason about transfers and synchronization

Memory-space declarations describe where data may reside and which workers may observe it. Global memory is broadly visible and typically high latency. Shared memory supports cooperation within a declared scope. Local memory may mean thread-private storage or backend-managed spill space, so the profile must define it precisely.

Layout maps logical indexes to physical order. Stride measures address movement per logical step. Two tensors can share a shape while differing in layout, contiguity, padding, and alignment. A compiler that rewrites layout must update addressing and preserve aliasing behavior. Device transfer adds source/destination identity, synchronization, lifetime, and failure handling.

The language’s explicit memory vocabulary makes optimization review possible. A promoted shared-memory tile is only correct when loading, barriers, indexing, and visibility are all proven.

## Worked corpus example

**Corpus anchor:** `DMK-00423` · `beginner` · `negative`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_00423
use DeepMLKernel
policy no_network

kernel DMK_00423(input: Tensor<f32>[37,64]) -> Tensor<f32>[37,64]
target cpu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..37 tile 32 {
        vectorize 16
        output[i] = input[i] * 21.0
    }
}
verify bounds with unchecked
assert kernel.race_free == false
emit kernel "DMK_00423.dmk"
```

## Laboratory

Rewrite a global-memory kernel to stage data in shared memory. Add loading, barrier, computation, and tail steps. Document every race and bounds obligation.

## Review questions

1. Why are shape and stride separate concepts?
2. What scope does a barrier need for shared memory?
3. Which evidence should accompany a device transfer?


---

# Chapter 8: Bounds, Barriers, Atomics, and Race Freedom

## Learning objectives

- Define bounds and race proof obligations
- Use barriers and atomics only with explicit scope
- Distinguish prevention from detection

Bounds safety proves that every memory access lands inside an authorized object for all admissible indexes. Race freedom proves that conflicting accesses are ordered or otherwise safe. These are different properties: an in-bounds write can still race, and a race-free access can still be out of bounds.

Barriers order participating workers at a scope. They are unsafe when control flow allows some required participants to skip them. Atomics make a transition indivisible according to a memory-order contract; they do not automatically make a larger algorithm deterministic. Race analysis must include aliases, address spaces, launch geometry, and reduction semantics.

Negative and security records intentionally use `verify bounds with unchecked` or assert that race freedom is false. A conforming implementation should reject such paths with the expected diagnostic rather than quietly emitting an artifact.

## Worked corpus example

**Corpus anchor:** `DMK-00243` · `beginner` · `positive`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_00243
use DeepMLKernel
policy no_network

kernel DMK_00243(input: Tensor<f32>[51,64]) -> Tensor<f32>[51,64]
target cpu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..51 tile 32 {
        vectorize 16
        output[i] = input[i] * 27.0
    }
}
verify bounds with checked
assert kernel.race_free == true
emit kernel "DMK_00243.dmk"
```

## Laboratory

Analyze one rejected script. Identify the exact unsafe access or ordering assumption, propose the smallest repair, and preserve the original diagnostic in the repair report.

## Review questions

1. Can an atomic operation still produce nondeterministic results?
2. Why may a barrier diverge?
3. What inputs are required for a bounds proof?


---

# Chapter 9: Reductions and Custom Operators

## Learning objectives

- Describe reduction identities and ordering
- Explain why floating-point reductions need tolerance contracts
- Define registration obligations for custom operators

A reduction combines many values into one or fewer values. Its contract includes the operator, identity element, axes or domain, ordering requirements, empty-domain behavior, accumulator type, and numerical tolerance. Integer addition may be associative only under an overflow policy; floating-point addition is not mathematically associative in finite precision.

Parallel reductions trade fixed order for concurrency. A reproducible profile may require a canonical tree, compensated accumulation, or exact accumulator. A fast profile may allow backend-dependent trees within a tolerance. The choice must be explicit and recorded.

Custom operators extend the language but also expand its trusted computing base. Registration should provide a signature, shape function, effect and capability set, device implementations, reference semantics, derivative rule when relevant, deterministic class, diagnostics, conformance tests, and versioned identity.

## Worked corpus example

**Corpus anchor:** `DMK-00148` · `beginner` · `positive`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_00148
use DeepMLKernel
policy no_network

kernel DMK_00148(input: Tensor<f32>[53,16]) -> Tensor<f32>[53,16]
target gpu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..53 tile 16 {
        vectorize 16
        output[i] = input[i] * 25.0
    }
}
verify bounds with checked
assert kernel.race_free == true
emit kernel "DMK_00148.dmk"
```

## Laboratory

Implement a specification—not executable code—for a deterministic sum reduction and a custom normalized-clamp operator. Include shape, effect, precision, derivative, and conformance clauses.

## Review questions

1. Why is an identity element part of a reduction contract?
2. How can a reduction be reproducible across devices?
3. What must a custom operator register besides code?


---

# Chapter 10: AST, Semantic Judgments, Effects, and Capabilities

## Learning objectives

- Follow source into AST and semantic interpretation
- Distinguish effects from capabilities
- Explain policy admission and proof obligations

The AST represents structure with stable node identity and source spans. Semantic interpretation assigns meaning: declared and inferred type, effects, required capabilities, policy decision, proof obligations, and a formalized judgment string. These fields create a review surface between parsing and lowering.

An effect describes what execution may do, such as state write or device action. A capability describes authority or resources required, such as CPU execution or shared memory. Policy decides whether the combination is admitted. A valid type does not override a denied policy, and an available capability does not prove race freedom.

Stable identities matter when optimizations fold or clone nodes. The compiler may create derived nodes, but it must preserve origin links so R12 and MCRT records can explain how the artifact came from source.

## Worked corpus example

**Corpus anchor:** `DMK-03527` · `expert` · `negative`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_03527
use DeepMLKernel
policy no_network

kernel DMK_03527(input: Tensor<f32>[37,64]) -> Tensor<f32>[37,64]
target npu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..37 tile 32 {
        vectorize 16
        output[i] = input[i] * 25.0
    }
}
verify bounds with unchecked
assert kernel.race_free == false
emit kernel "DMK_03527.dmk"
```

## Laboratory

Select one accepted and one rejected record. Draw the chain from AST node to judgment, effects, capabilities, policy, proof obligations, R12 state, and runtime result.

## Review questions

1. How do effects differ from capabilities?
2. Can a well-typed program be policy-denied?
3. Why must compiler-generated nodes retain origin links?


---

# Chapter 11: Backend Lowering and Device Targets

## Learning objectives

- Define lowering as semantics-preserving translation
- Identify backend capability checks
- Separate specialization from source meaning

Backend lowering converts language operations into a device representation. A target may support different vector widths, memory spaces, atomics, barriers, numerical formats, and launch constraints. Lowering is therefore a proof-bearing translation, not a textual rewrite.

Device specialization may choose layouts, tiles, instructions, workgroup shapes, or fused operations. It must preserve source-visible behavior and record backend assumptions. When a device lacks a required feature, the compiler may select a compatible fallback only if policy permits and the artifact identity records that decision.

Interoperability examples test movement between profiles and components. A backend adapter should validate version, type layout, effects, capabilities, numerical profile, and provenance rather than accepting an opaque blob.

## Worked corpus example

**Corpus anchor:** `DMK-00487` · `beginner` · `negative`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_00487
use DeepMLKernel
policy no_network

kernel DMK_00487(input: Tensor<f32>[4,64]) -> Tensor<f32>[4,64]
target gpu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..4 tile 32 {
        vectorize 16
        output[i] = input[i] * 23.0
    }
}
verify bounds with unchecked
assert kernel.race_free == false
emit kernel "DMK_00487.dmk"
```

## Laboratory

Draft a lowering record for the same kernel on CPU, GPU, and NPU. Identify common semantics and backend-specific evidence.

## Review questions

1. What makes lowering more than code generation?
2. When may a compiler choose a fallback device?
3. Which assumptions belong in artifact identity?


---

# Chapter 12: R12 Lowering and MCRT Provenance

## Learning objectives

- Explain the role of R12 and MCRT records
- Trace hashes and identity across compilation and runtime
- Define replay-preserving transformations

R12 is the suite’s compiler-side evidence record. It ties a statement and AST node to a language profile, semantic operator, dependencies, type, effects, capabilities, policy, hashes, state, error status, confidence, proof status, source location, and canonical tuple. MCRT is the runtime/provenance companion that ties source hash, AST, semantic judgment, R12 identity, deterministic class, policy, confidence, certification status, and a canonical record.

The pair is useful because source code alone cannot explain which policy was applied, which lowering occurred, or why execution was blocked. Conversely, runtime telemetry without source and semantic identity is difficult to audit.

Replay does not require byte-for-byte identical internal implementation, but it does require invariant evidence. A folded or optimized program must preserve contradiction, uncertainty, provenance, projection profile, interaction order, error state, and declared tolerance-sensitive results.

## Worked corpus example

**Corpus anchor:** `DMK-01801` · `intermediate` · `security`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_01801
use DeepMLKernel
policy no_network

kernel DMK_01801(input: Tensor<f32>[57,32]) -> Tensor<f32>[57,32]
target gpu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..57 tile 32 {
        vectorize 16
        output[i] = input[i] * 4.0
    }
}
verify bounds with unchecked
assert kernel.race_free == false
emit kernel "DMK_01801.dmk"
```

## Laboratory

Pick a script and manually construct a minimal R12/MCRT pair using the schema. Then describe which fields change after a legal tile-size optimization.

## Review questions

1. Which record is compiler-facing and which is runtime-facing?
2. Why are both input and output hashes useful?
3. What must remain invariant after canonicalization?


---

# Chapter 13: Precision, Determinism, and Tolerance Equivalence

## Learning objectives

- Distinguish exact equality from tolerance equivalence
- Describe sources of device nondeterminism
- Design a versioned numerical profile

Numerical equivalence depends on type, operation, order, backend, and tolerance. Strict precision can require fixed operation order and limited contraction. Balanced precision may allow selected fused operations. Fast precision may allow broader reassociation and approximations. These names are insufficient unless a versioned profile defines them.

Nondeterminism can arise from atomic update order, parallel reduction trees, race conditions, uninitialized memory, backend scheduling, random inputs, algorithm selection, and external state. Declaring `reproducible` creates obligations across compiler and runtime; it does not magically satisfy them.

Tolerance equivalence should specify absolute, relative, and sometimes ULP limits; NaN and infinity behavior; shape and mask handling; accumulation precision; and statistical criteria for stochastic operations. Certification records are the correct place to lock these decisions to a version.

## Worked corpus example

**Corpus anchor:** `DMK-00137` · `beginner` · `positive`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_00137
use DeepMLKernel
policy no_network

kernel DMK_00137(input: Tensor<f32>[42,32]) -> Tensor<f32>[42,32]
target npu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..42 tile 32 {
        vectorize 16
        output[i] = input[i] * 14.0
    }
}
verify bounds with checked
assert kernel.race_free == true
emit kernel "DMK_00137.dmk"
```

## Laboratory

Create strict, balanced, and fast numerical profiles for one reduction. State allowed transformations and pass/fail comparisons.

## Review questions

1. Why can two race-free runs still differ numerically?
2. What does ULP measure?
3. Which tolerance rules must address NaN values?


---

# Chapter 14: Autodiff Primitives and Kernel Fusion

## Learning objectives

- State primal and derivative contracts
- Explain fusion benefits and semantic hazards
- Preserve debugging and provenance through fused kernels

An autodiff primitive needs a primal definition, input/output types and shapes, derivative rule, nondifferentiable-point policy, saved intermediates, precision behavior, device implementations, and tests. A derivative kernel is not valid merely because it compiles; it must match reference mathematics within a declared tolerance.

Fusion combines operations to reduce memory traffic and launch overhead. It can also change rounding, exception timing, intermediate precision, memory lifetime, synchronization, and diagnostic granularity. The compiler should fuse only when the numerical and effect contracts permit it.

Provenance should map a fused artifact back to every contributing source node and semantic operator. Debug modes may retain unfused boundaries or provide synthetic source maps so a failure remains explainable.

## Worked corpus example

**Corpus anchor:** `DMK-00437` · `beginner` · `negative`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_00437
use DeepMLKernel
policy no_network

kernel DMK_00437(input: Tensor<f32>[51,32]) -> Tensor<f32>[51,32]
target npu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..51 tile 32 {
        vectorize 16
        output[i] = input[i] * 4.0
    }
}
verify bounds with unchecked
assert kernel.race_free == false
emit kernel "DMK_00437.dmk"
```

## Laboratory

Specify and test the derivative of `y = x*x + 2*x`. Then propose a fused kernel and document numerical, identity, and diagnostic differences.

## Review questions

1. What belongs in an autodiff primitive contract?
2. How can fusion alter floating-point results?
3. Why does a fused artifact need many-to-one provenance?


---

# Chapter 15: Diagnostics, Negative Tests, and Recovery

## Learning objectives

- Treat rejected programs as language-definition assets
- Design stable, actionable diagnostics
- Separate repair from suppression

Negative examples define what the language refuses. Their expected diagnostic code is part of conformance. A good diagnostic identifies the failed contract, source location, relevant type or capability, expected state, observed state, and safe repair direction without exposing secrets.

Recovery examples test whether tooling can continue after an error, propose a bounded repair, or select a compatible configuration. Recovery must retain the original evidence and must not turn a denied policy into silent acceptance. Automated repair should produce a patch and a new validation result, not overwrite history.

The suite includes a generated diagnostic catalog so implementers can see code frequency and associated feature classes. A future native compiler should map its diagnostics to these stable identifiers or publish a versioned translation table.

## Worked corpus example

**Corpus anchor:** `DMK-00544` · `beginner` · `negative`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_00544
use DeepMLKernel
policy no_network

kernel DMK_00544(input: Tensor<f32>[61,16]) -> Tensor<f32>[61,16]
target gpu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..61 tile 16 {
        vectorize 16
        output[i] = input[i] * 18.0
    }
}
verify bounds with unchecked
assert kernel.race_free == false
emit kernel "DMK_00544.dmk"
```

## Laboratory

Select five diagnostic codes from the catalog. For each, write a minimal failing case, an actionable message, and a repair that changes only the necessary contract.

## Review questions

1. Why are negative tests essential to conformance?
2. What makes a diagnostic stable?
3. How should repair provenance be recorded?


---

# Chapter 16: Security, Offline Policy, and Deployment

## Learning objectives

- Explain the `no_network` baseline
- Identify deployment-time trust boundaries
- Keep blocked artifacts nonexecutable

Every curated program carries `policy no_network`. The runtime contract also forbids hidden network execution and requires secret redaction. This makes offline operation a baseline rather than an optional hardening step.

Deployment introduces artifact signing, backend compatibility, driver and runtime identity, capability grants, memory isolation, input validation, resource limits, diagnostic redaction, rollback, and audit retention. A compiler-approved artifact can still be inappropriate for a particular device or security domain.

Security records are expected failures when bounds are unchecked, race freedom is false, policy is denied, or required evidence is missing. The release preserves them because a secure system must prove it can refuse work, not only execute it.

## Worked corpus example

**Corpus anchor:** `DMK-00190` · `beginner` · `positive`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_00190
use DeepMLKernel
policy no_network

kernel DMK_00190(input: Tensor<f32>[95,48]) -> Tensor<f32>[95,48]
target gpu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..95 tile 32 {
        vectorize 16
        output[i] = input[i] * 5.0
    }
}
verify bounds with checked
assert kernel.race_free == true
emit kernel "DMK_00190.dmk"
```

## Laboratory

Write a deployment checklist for an air-gapped GPU workstation. Include artifact verification, runtime identity, input handling, capability binding, logging, rollback, and prohibited behavior.

## Review questions

1. What does no-network prohibit beyond HTTP calls?
2. Why must a denied artifact have no executable output?
3. Which deployment checks occur after compilation?


---

# Chapter 17: Performance Engineering Without Semantic Drift

## Learning objectives

- Use measurement hypotheses rather than folklore
- Connect performance features to correctness constraints
- Design reproducible benchmark evidence

Performance work begins with a bottleneck hypothesis: memory bandwidth, latency, occupancy, vector utilization, synchronization, launch overhead, instruction throughput, transfer cost, or compilation specialization. Each hypothesis suggests a measurement and a bounded transformation.

The language exposes many levers—tiling, vectorization, SIMD, fusion, layout, stride, shared memory, precision, target, reduction structure, and launch dimensions. None is universally beneficial. A transformation can increase register pressure, reduce occupancy, add bank conflicts, worsen tails, or violate determinism.

A benchmark report should record source and artifact hashes, compiler/runtime/backend versions, device identity, input distribution, warm-up, repetitions, synchronization, timing method, numerical comparison, variance, and resource counters. Since no native runtime was supplied, this release does not fabricate benchmark numbers.

## Worked corpus example

**Corpus anchor:** `DMK-00008` · `beginner` · `positive`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_00008
use DeepMLKernel
policy no_network

kernel DMK_00008(input: Tensor<f32>[10,16]) -> Tensor<f32>[10,16]
target npu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..10 tile 16 {
        vectorize 16
        output[i] = input[i] * 9.0
    }
}
verify bounds with checked
assert kernel.race_free == true
emit kernel "DMK_00008.dmk"
```

## Laboratory

Design a benchmark plan comparing unfused and fused kernels. Define correctness gates and the evidence required before claiming improvement.

## Review questions

1. What is a performance hypothesis?
2. Why can a larger tile be slower?
3. Which metadata makes a benchmark reproducible?


---

# Chapter 18: Smithson 8S Coupled Mechanics Profile

## Learning objectives

- State the model with its supplied scientific limitations
- Explain how coupling annotations attach to kernel evidence
- Apply admission and observability gates

The source corpus embeds **Smithson 8S Coupled Mechanics v1.0** as a proposed generative and computational model. The corpus itself correctly states that it is not an established physical law, not automatically the standard sphere `S^8`, and not evidence of physical quantum entanglement. This textbook preserves that status boundary.

The model describes an `S^3` fiber over a five-dimensional penteract base, activation and phase coupling, sparse pairwise neighborhoods, selective triadic escalation, projection tests, semantic distance, and R12 replay invariants. Its admission gate compares a seven-coordinate model with an eight-coordinate extension through a nonredundancy score `eta_ind` and held-out efficacy gain `Delta_8S`.

For kernel engineering, the useful idea is not a physical claim but an evidence discipline: keep latent state, projected state, semantic relation, uncertainty, interaction order, provenance, and replay identity separate. A projection-only overlap must not be reported as latent coupling. A higher-order result must record the triadic term that changed the pairwise classification.

Implementation should use sparse pairwise neighborhoods and activate triadic terms only for unresolved, contradictory, high-risk, or certification-critical clusters. This avoids unrestricted cubic cost while retaining an escalation path.

## Worked corpus example

**Corpus anchor:** `DMK-03527` · `expert` · `negative`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_03527
use DeepMLKernel
policy no_network

kernel DMK_03527(input: Tensor<f32>[37,64]) -> Tensor<f32>[37,64]
target npu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..37 tile 32 {
        vectorize 16
        output[i] = input[i] * 25.0
    }
}
verify bounds with unchecked
assert kernel.race_free == false
emit kernel "DMK_03527.dmk"
```

## Laboratory

Using synthetic—not empirical—data, compute an independence score and draft an admission decision. Clearly label assumptions and list evidence still required for scientific validation.

## Review questions

1. What status limitation accompanies the 8S model?
2. Why are projected and latent relations separated?
3. What evidence is required before admitting an eighth coordinate?


---

# Chapter 19: Conformance and Certification Engineering

## Learning objectives

- Build a layered conformance strategy
- Use the full corpus rather than only curated examples
- Report mismatches with reproducible evidence

Conformance is layered. A record validator checks schema and identity. A parser checks source syntax. Semantic tests check types, shapes, effects, capabilities, policy, bounds, races, and diagnostics. Lowering tests compare accepted artifacts and rejected non-artifacts. Runtime tests validate capability binding, numerical results, deterministic class, sandbox behavior, and replay evidence.

The 1,000-script pack is designed for teaching and fast smoke tests. Certification should use all 10,000 records because the full distribution contains substantially more combinations. Expected status and diagnostic code are the primary outcome fields; accepted records also need artifact and runtime evidence.

A conformance report names the exact suite version, compiler, runtime, backend, device, profile, failed record IDs, observed outcomes, expected outcomes, and attached logs. Partial support should be represented as a profile, not described as full conformance.

## Worked corpus example

**Corpus anchor:** `DMK-00514` · `beginner` · `negative`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_00514
use DeepMLKernel
policy no_network

kernel DMK_00514(input: Tensor<f32>[31,48]) -> Tensor<f32>[31,48]
target gpu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..31 tile 32 {
        vectorize 16
        output[i] = input[i] * 19.0
    }
}
verify bounds with unchecked
assert kernel.race_free == false
emit kernel "DMK_00514.dmk"
```

## Laboratory

Draft a conformance runner architecture that can parse catalogs, invoke a future compiler, capture artifacts/diagnostics, run accepted kernels, and emit a machine-readable report.

## Review questions

1. Why is the teaching pack insufficient for certification?
2. What is a conformance profile?
3. Which mismatch fields make a failure reproducible?


---

# Chapter 20: Capstone: A Standalone Kernel Toolchain

## Learning objectives

- Plan a parser-to-runtime vertical slice
- Integrate safety, provenance, and education assets
- Define a release gate for version 1.1

The capstone is a minimal but complete DeepML Kernel toolchain: parser, formatter, AST, semantic checker, diagnostic engine, R12 lowering, reference interpreter or CPU backend, MCRT writer, corpus runner, and report generator. Start with the observed canonical syntax and a small positive/negative feature set. Expand only when the existing slice is replayable.

A strong first milestone accepts a simple static tensor map, rejects one bounds violation, emits a stable AST and R12 record, executes on a deterministic CPU reference backend, writes MCRT evidence, and compares the result with a reference array. The second milestone adds symbolic shapes, tiling, and a deterministic reduction. The third adds device adapters and conformance profiles.

Version 1.1 should not be gated by the number of features alone. It should require stable grammar, round-trip formatting, clear diagnostics, no-network enforcement, source-to-runtime provenance, reproducible tests, a migration note, regenerated catalogs, and a validation report that distinguishes modeled from executed evidence.

## Worked corpus example

**Corpus anchor:** `DMK-00031` · `beginner` · `positive`

```dmk
ja source 0.3
module corpus.deepml_kernel.example_00031
use DeepMLKernel
policy no_network

kernel DMK_00031(input: Tensor<f32>[33,64]) -> Tensor<f32>[33,64]
target gpu
precision strict
determinism reproducible
memory global
{
    parallel for i in 0..33 tile 32 {
        vectorize 16
        output[i] = input[i] * 1.0
    }
}
verify bounds with checked
assert kernel.race_free == true
emit kernel "DMK_00031.dmk"
```

## Laboratory

Create a project plan with components, interfaces, test gates, and release evidence for the first vertical slice. Implement at least the parser and structural validator against the starter program.

## Review questions

1. What is the smallest credible vertical slice?
2. Why should a reference backend precede aggressive device optimization?
3. Which evidence should gate version 1.1?


---

# Glossary

**Artifact** — Compiler output admitted for a declared runtime profile.  
**AST** — Structured source representation with stable nodes and spans.  
**Capability** — Authority or resource required to perform an operation.  
**Determinism class** — Versioned statement of reproducibility guarantees.  
**Effect** — Observable action a kernel may perform.  
**Kernel fusion** — Combining operations or kernels to reduce intermediate work.  
**Layout** — Mapping from logical indexes to physical storage order.  
**MCRT** — Runtime/provenance evidence linked to source, semantics, and R12.  
**Policy decision** — Admission result for types, effects, capabilities, and environment.  
**R12** — Compiler-side canonical evidence record.  
**Race freedom** — Absence of unsafe conflicting concurrent accesses.  
**Stride** — Physical address step associated with a logical index step.  
**Tolerance equivalence** — Equality under a declared numerical comparison profile.  
**Modeled not executed** — Expected result encoded by the corpus without native execution evidence.

# Appendix A: Corpus feature inventory

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

# Appendix B: Validation class inventory

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

# Appendix C: Publication limitations

This suite does not include a native compiler, runtime, device backend, empirical benchmark, or scientific validation dataset. It offers a normalized corpus, curated examples, contracts, educational material, structural tools, and a precise target for future implementation.
