# LLM-K

LLM K (LLM Kaizen Language) is an AI-first programming language designed for both humans and Large Language Models (LLMs).

LLM K explores how programming languages can be designed when LLMs are treated as first-class participants in software development.

The language prioritizes:

- Simplicity
- Explicit behavior
- Predictable program structure
- Deterministic semantics
- Maintainability
- Human–LLM collaboration

The goal is not to create a language only for AI, but to provide a common programming language that both humans and LLMs can understand, generate, modify, and maintain.

## Why LLM K?

LLMs are increasingly involved in software development, including:

- Code generation
- Code modification
- Refactoring
- Code review
- Testing
- Debugging
- Long-term software maintenance
- Autonomous or semi-autonomous software development

Existing programming languages can be used for these tasks, but they were not necessarily designed with LLM-based development as a primary consideration.

LLM K explores a different design space: a programming language whose structure is intentionally designed to reduce unnecessary ambiguity and make software easier to reason about for both humans and LLMs.

## Documentation

### Language Specification

The language specification defines the syntax and semantics of LLM K.

**[Language Specification](language-specification/README.md)**

The specification is divided into multiple files so that individual sections can be read and maintained independently.

### Design Rationale

Explains why the language was designed this way, including the reasoning behind its major design decisions.

**[Design Rationale](docs/design-rationale.md)**

### Purpose and Use Cases

Explains the purpose of LLM K, its intended users, and the software development workflows it is designed to support.

**[Purpose and Use Cases](docs/purpose-and-use-cases.md)**

### Development Plan

Describes the staged path from the language specification to a reference
implementation.

**[Development Plan](docs/development-plan.md)**

## Current Status

LLM K is currently a language design project with an early Python reference
implementation.

The reference implementation currently provides a Lexer, Parser, AST, static
type checker, deterministic Interpreter, and initial CLI.

The implementation is intentionally incomplete while the language
specification is being stabilized.

## Quick Start

Install the project and development dependencies with `uv`:

```text
uv sync
```

Check and run the example program:

```text
uv run llmk check examples/counter.llmk
uv run llmk run examples/counter.llmk Counter.Create 4
```

Run the test suite:

```text
uv run pytest
```

## Design Philosophy

LLM K follows several principles:

### Explicitness over implicit behavior

Important program behavior should be visible in the source code.

### Simplicity over unnecessary flexibility

The language intentionally restricts some constructs when doing so makes program structure easier to understand and reason about.

### Predictability over convenience

Programs should have clear and predictable semantics for both humans and LLMs.

### Common representation for humans and AI

The same source code should serve as the representation shared by human developers and LLMs.

## Project Structure

```text
llm-k/
├── README.md
├── language-specification/
│   ├── README.md
│   └── ...
└── docs/
    ├── design-rationale.md
    └── purpose-and-use-cases.md
```

## Contributing

LLM K is developed specification-first. See [Contributing](CONTRIBUTING.md)
for change guidelines and [Development Plan](docs/development-plan.md) for the
implementation roadmap.

Discussion, review, and experimentation are welcome.

## License

LLM K is licensed under the Apache License 2.0.

See [LICENSE](LICENSE) for the full license text.
