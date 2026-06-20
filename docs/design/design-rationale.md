# Design Rationale for ai-kaizen-lang

## Problem Statement

Existing programming languages were designed for human programmers or optimizers. ai-kaizen-lang is designed specifically to be understood by both humans and AI language models (LLMs).

## Key Design Decisions

### 1. Single-Operation Expressions

**Decision:** Limit expressions to exactly one operation.

**Rationale:**
- Prevents LLM misinterpretation of operator precedence
- Maintains clarity for human readers
- Enforces explicit intermediate steps

### 2. Explicit Type System

**Decision:** Require explicit type annotations everywhere.

**Rationale:**
- Eliminates type inference ambiguity
- LLMs must see the full type picture
- Reduces subtle bugs

### 3. No Implicit Type Conversion

**Decision:** Forbid all implicit type conversions.

**Rationale:**
- LLMs often misinterpret implicit conversions
- Explicit conversions make intent clear
- Easier to reason about code behavior

### 4. Reference Semantics via REF

**Decision:** Default to value semantics; use REF for references.

**Rationale:**
- Value semantics are easier to understand
- Makes side effects explicit
- Prevents subtle sharing bugs

### 5. Unified Error Handling

**Decision:** Single error propagation model.

**Rationale:**
- LLMs don't confuse different error mechanisms
- Consistent error handling everywhere
- Easier to audit error paths

## Trade-offs

- **Verbosity vs. Clarity:** We choose clarity. Explicit code is easier for LLMs.
- **Expressiveness vs. Safety:** We choose safety. Constraints prevent misuse.
- **Flexibility vs. Consistency:** We choose consistency. Same operation = same notation.

## Future Directions

- Phase 2: Self-hosting (aikai written in aikai)
- Phase 3: Native compilation
- Phase 4: Ecosystem and libraries
