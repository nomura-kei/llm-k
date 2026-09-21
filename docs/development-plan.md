# LLM K Development Plan

This document describes how to move LLM K from a language specification to a
working implementation.

## Current Implementation Status

The repository currently contains the first executable slice of the reference
implementation:

- Lexer and source locations.
- AST and recursive-descent parser.
- Initial name and type checks.
- Deterministic interpreter for literals, variables, expressions, calls, TYPE
  construction, and assignment.
- `check` and `run` CLI commands.

The implementation does not yet cover all grammar productions, imports across
files, MATCH, FOR, PARFOR, or the standard library.

## Implementation Strategy

The first implementation should be a small reference implementation with a
clear compiler pipeline:

```text
.llmk source
    -> lexer
    -> parser and AST
    -> name resolution
    -> type checking
    -> interpreter
    -> CLI diagnostics and exit status
```

An interpreter is preferred for the first executable implementation. It gives
the language design fast feedback without requiring a code generator or native
runtime. A compiler backend can be added after the semantics are stable.

The host language and build system should be selected in a separate decision
before implementation files are created. The selection should prioritize
parser and testing support, reliable diagnostics, portability, and ease of
maintenance.

## Phase 0: Specification Readiness

Before writing the lexer, resolve the parts of the specification that affect
the complete parser or type checker:

- Define the complete token set, including assignment, member access, and
  function-call syntax.
- Define indentation, blank-line, and multi-line construct rules.
- Complete the grammar for assignment, calls, constructors, and MATCH cases.
- Define name resolution and import search rules.
- Define type compatibility, mutability, REF behavior, and assignment rules.
- Define runtime representation for OPTIONAL, RESULT, ARRAY, and NONE.
- Define diagnostics: source locations, error categories, formatting, and exit
  codes.
- Separate language semantics from standard-library behavior.

Each decision should be recorded in the relevant specification chapter and
covered by at least one valid or invalid example.

## Phase 1: Executable Foundation

Create the implementation workspace and a command-line entry point. The first
milestone should accept a `.llmk` file, report lexical or syntax errors with
source locations, and exit with a non-zero status for invalid input.

Deliverables:

- Host-language project and reproducible build command.
- Source file loader with UTF-8 and LF/CRLF support.
- Token model and lexer.
- AST data model.
- Recursive-descent or equivalent parser.
- Golden tests for tokens, ASTs, and diagnostics.

## Phase 2: Static Semantics

Implement the rules that can be checked without executing a program:

- Module and TYPE identity.
- Explicit imports and qualified function calls.
- Duplicate and unresolved names.
- Variable declaration and LET/VAR mutability.
- Function parameters and inferred final return values.
- Built-in types and type modifiers.
- Constructor field order and TYPE dependency cycles.
- REF parameter restrictions.

The type checker should produce structured diagnostics so tests do not depend
on terminal formatting.

## Phase 3: Reference Runtime

Implement a deterministic interpreter for the statically valid subset:

- Literal and expression evaluation.
- Variable bindings and assignment.
- TYPE construction and member access.
- Qualified function calls.
- IF and MATCH.
- FOR with deterministic iteration.
- OPTIONAL and RESULT values.

PARFOR should remain unavailable or explicitly rejected until its scheduling,
ordering, REF restrictions, and error behavior are fully specified.

## Phase 4: Standard Library and Usability

Define the standard-library interface separately from the core language, then
add only the smallest useful modules. Add a formatter, example programs, and a
tutorial after the syntax and diagnostics have stabilized.

## Phase 5: Conformance and Evolution

Maintain a conformance suite containing valid programs, invalid programs, and
expected diagnostics. Every specification change should update the suite and
state whether it is compatible with existing programs.

Track implementation status by feature rather than by file count. A feature is
complete only when its specification, implementation, tests, and documentation
agree.

## First Milestone

The first practical milestone is a `check` command that can parse and type
check a small program containing:

- One module and one TYPE.
- Primitive fields and TYPE construction.
- A function with parameters and a final expression.
- LET declarations.
- A qualified function call.
- A useful source-location diagnostic for one invalid program.

The interpreter should be added immediately after this milestone so language
decisions are tested against observable behavior rather than syntax alone.

## Definition of Done

For each language feature:

1. The specification defines valid behavior and invalid behavior.
2. The lexer, parser, checker, and runtime agree on the behavior.
3. Positive and negative tests cover the feature.
4. Diagnostics identify the source location and the violated rule.
5. At least one small example demonstrates intended usage.