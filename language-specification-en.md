# ai-kaizen-lang (aikai) Spec v1.0

## 1. Design Principles

- Syntax is simple and unambiguous
- No syntactic sugar
- Same operation uses same notation
- Implicit behavior is prohibited
- Priority: LLM must not misinterpret

---

## 2. Naming Conventions

- Reserved words: UPPERCASE
- Identifiers: lowercase_snake_case
- Comments: `#` at line start only

---

## 3. Statements

- 1 line = 1 statement
- No line breaks in the middle

---

## 4. Types

### Primitive Types
- INT
- STRING
- BOOL

### Composite Types
- ARRAY ! TYPE
- STRUCT name ... END STRUCT

### Special Types
- REF TYPE
- TASK TYPE

---

## 5. Type System

- Fully static typing
- Completely explicit typing
- Nominal type system (STRUCT identified by name)
- Only exact type matching permitted
- No implicit type conversion

---

## 6. Values and Expressions

### value
- Literal
- Variable
- Function call result
- STRUCT initialization

### expr
- value OP value

### Constraints
- expr has exactly one operation
- No nesting
- value is not expr
- Complex calculations decomposed with LET

---

## 7. Operators

- Arithmetic: + - * / %
- Comparison: == != < <= > >=
- Logical: && ||
- Bitwise: & | ^ << >>

---

## 8. Variables
LET TYPE name = value_or_expr VAR TYPE name = value_or_expr

- Type required
- Initialization required
- LET is immutable
- VAR is reassignable

---

## 9. Assignment
name = value_or_expr

- Only VAR allowed

---

## 10. Control Flow

### IF
IF condition statements ELSE statements END IF

- condition must be BOOL only

---

### FOR
FOR array AS item statements END FOR

- ARRAY only

---

## 11. Functions

### Definition
TYPE FUNC name PARAM TYPE param ... statements RETURN value_or_expr END FUNC

### Invocation
LET TYPE v = func arg1 arg2

### Constraints

- Arguments must be values (expr prohibited)
- Single return value only

---

## 12. ERROR Handling

### ERROR Function
TYPE FUNC name ... ERROR

### raise
std.error.raise "ERROR_CODE"

### ERROR Block
FUNC ... statements ERROR err handler END FUNC

### Rules

- raise always propagates
- Cannot be caught in same function
- ERROR caught by caller function only
- Non-ERROR function calling ERROR function requires ERROR block

### State

- ERROR does not roll back state

---

## 13. Resource Management

- Automatic deallocation at scope end
- Deallocation on ERROR
- Deallocation order is LIFO

---

## 14. Memory Model

- All pass-by-value
- Reference via REF
- Side effects via REF only

### REF Constraints

- REF applies to VAR only
- Only VAR can be passed to REF argument

---

## 15. STRUCT

### Definition
STRUCT name TYPE field END STRUCT

### Initialization
LET name v = { value1, value2 }

- Order must match
- No omission

### Properties

- Immutable (field modification prohibited)

---

## 16. ARRAY

- Elements must be same type
- Type must be explicit

---

## 17. Parallelism

### spawn
LET TASK TYPE t = std.task.spawn func arg1 arg2

### join
LET TYPE v = std.task.join t

---

### Parallelism Rules

- spawn allows ERROR functions
- Arguments evaluated and copied at spawn time
- ERROR occurs at join time
- Unjoined threads implicitly joined at scope end
- Implicit join still raises ERROR
- After ERROR, subsequent operations not executed
- REF arguments prohibited in parallel functions
- Side effects (IO) allowed
- Side effect order undefined

---

## 18. Cancellation
std.task.cancel t

- Raises "CANCELLED" at join
- Occurs at observation points only

---

## 19. Modules
IMPORT full.path.module AS alias

- Full path required
- Circular references prohibited

---

## 20. Prohibited

- Syntactic sugar
- Implicit type conversion
- expr nesting
- Compound expressions
- expr in function arguments
- Ambiguous shared state
- REF use in parallelism

---

## 21. Syntax (EBNF)

### expr
expr = value operator value ;

### value
value = literal | identifier | func_call | struct_literal ;

### func_call
identifier value...

---

## 22. Execution Model

- AST-based execution
- ERROR is exceptional control flow
- Parallelism synchronizes at join

---

## 23. Compiler Structure

1. Lexer
2. Parser
3. AST generation
4. Type checking
5. ERROR validation
6. Parallelism constraint validation
7. Execution

---

## 24. Design Essence

- Expressions limited to single operation
- Side effects restricted to REF
- ERROR unified to single path
- Parallelism restricted conservatively

---

## 25. Features

- Zero ambiguity
- Maximum LLM resistance to misinterpretation
- Easy to implement
- Parallel safe
