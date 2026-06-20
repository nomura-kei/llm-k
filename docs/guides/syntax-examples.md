# ai-kaizen-lang Syntax Examples

This document provides practical examples of ai-kaizen-lang syntax.

## Variables

### Immutable Variables (LET)

```aikai
LET INT x = 42
LET STRING name = "Alice"
LET BOOL flag = 1 == 1
```

### Mutable Variables (VAR)

```aikai
VAR INT counter = 0
counter = counter + 1
```

## Functions

### Simple Function

```aikai
INT FUNC add PARAM INT a PARAM INT b RETURN a + b END FUNC
```

### Function Call

```aikai
LET INT result = add 5 3
```

## Control Flow

### IF Statement

```aikai
IF x > 0 LET STRING msg = "positive" ELSE LET STRING msg = "non-positive" END IF
```

### FOR Loop

```aikai
LET ARRAY ! INT numbers = [1, 2, 3]
FOR numbers AS n LET INT doubled = n * 2 END FOR
```

## More Examples

See [examples/](../../examples/) directory for comprehensive examples.
