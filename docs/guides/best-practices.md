# ai-kaizen-lang Best Practices

## Design Principles

ai-kaizen-lang follows strict design principles to ensure clarity and prevent misinterpretation by LLMs.

### 1. Avoid Complex Expressions

❌ **Bad:**
```aikai
LET INT result = (a + b) * (c - d)
```

✅ **Good:**
```aikai
LET INT sum = a + b
LET INT diff = c - d
LET INT result = sum * diff
```

### 2. Use Explicit Types

❌ **Bad:**
```aikai
LET x = 42  # Type implicit
```

✅ **Good:**
```aikai
LET INT x = 42  # Type explicit
```

### 3. Handle Errors Explicitly

❌ **Bad:**
```aikai
STRING FUNC read_file PARAM STRING path RETURN std.io.read path END FUNC
```

✅ **Good:**
```aikai
STRING FUNC read_file PARAM STRING path ERROR RETURN std.io.read path ERROR err
  std.error.raise "FILE_READ_ERROR"
END FUNC
```

### 4. Prefer Immutability

❌ **Bad:**
```aikai
VAR INT counter = 0
counter = counter + 1
```

✅ **Good:**
```aikai
LET INT next_counter = counter + 1
```

## Performance Tips

1. Use parallel tasks for I/O operations
2. Minimize memory allocations in loops
3. Keep function scope small

See [language-specification.md](../../language-specification.md) for complete reference.
