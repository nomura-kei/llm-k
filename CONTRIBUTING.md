# Contributing to LLM K

LLM K is developed specification-first. Contributions should keep the
language understandable, deterministic, and maintainable for both humans and
LLMs.

## Before Changing the Language

1. Identify the affected specification chapter.
2. State the motivation and a concrete example.
3. Describe valid and invalid programs.
4. Consider compatibility and implementation complexity.
5. Update the specification before or together with the implementation.

Language changes should not be implemented only in parser behavior or tests.

## Implementation Rules

- Keep lexer, parser, static semantics, runtime, and CLI concerns separate.
- Prefer explicit data structures and structured diagnostics.
- Keep execution deterministic unless the specification explicitly permits
  otherwise.
- Add positive and negative tests for every new rule.
- Do not add standard-library behavior to the language core without a clear
  specification boundary.

## Validation

Every change should provide a reproducible validation command. At minimum,
run the formatter, unit tests, and the conformance suite when those tools are
available.

Documentation-only changes should still be checked for broken relative links
and contradictory statements.

## Commit Messages

Use a short, imperative, lowercase prefix where practical:

```text
spec: clarify RESULT matching semantics
parser: add qualified function calls
runtime: evaluate TYPE construction
docs: describe the implementation roadmap
test: add invalid assignment cases
```