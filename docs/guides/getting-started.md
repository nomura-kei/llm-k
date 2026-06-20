# Getting Started with ai-kaizen-lang

Welcome to ai-kaizen-lang (aikai).

This guide will help you set up the development environment and run your first aikai program.

## Prerequisites

- Python 3.9 or later
- Git

## Installation

```bash
git clone https://github.com/nomura-kei/ai-kaizen-lang.git
cd ai-kaizen-lang
pip install -e .
```

## Your First Program

Create a file `hello.aikai`:

```aikai
STRING FUNC main RETURN "Hello, ai-kaizen-lang!" END FUNC
```

Run it:

```bash
aikai hello.aikai
```

## Next Steps

- Read [language-specification.md](../../language-specification.md) for detailed syntax
- Check out [examples/](../../examples/) directory for more examples
- See [syntax-examples.md](./syntax-examples.md) for common patterns
