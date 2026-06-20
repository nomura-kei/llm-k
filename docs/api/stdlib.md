# ai-kaizen-lang Standard Library

## std.error

### raise

```aikai
std.error.raise "ERROR_CODE"
```

Raises an error with the given code.

## std.task

### spawn

```aikai
LET TASK INT t = std.task.spawn my_function arg1 arg2
```

Spawns a parallel task.

### join

```aikai
LET INT result = std.task.join t
```

Waits for task to complete and returns its result.

### cancel

```aikai
std.task.cancel t
```

Cancels a task.

## std.io

*(Planned)*

## std.array

*(Planned)*

More standard library functions will be documented as they are implemented.
