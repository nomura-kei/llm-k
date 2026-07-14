# LLM K (LLM Kaizen Language)
Language Specification

Version: 1.1 (Draft)

---

# 1. Introduction

## 1.1 Overview

LLM K (LLM Kaizen Language, abbreviated as LLMK) is a programming language designed primarily for Large Language Models (LLMs).

Unlike conventional programming languages, LLMK is designed with the assumption that source code is read, generated, modified, and maintained by both humans and AI.

The primary objective is to minimize ambiguity and reduce the probability of incorrect interpretation by LLMs while maintaining readability for human developers.

LLMK does not attempt to replace existing programming languages. Instead, it explores a language design optimized for AI-assisted software development.


The word "Kaizen" represents continuous improvement. LLMK is intended to evolve based on practical experience with AI-assisted software development while preserving its core design principles.

---

## 1.2 Goals

LLMK has the following goals.

- Minimize ambiguity.
- Reduce syntax complexity.
- Make program flow deterministic.
- Encourage modular and maintainable code.
- Reduce token consumption where it does not reduce readability.
- Optimize code understanding for both humans and LLMs.

---

## 1.3 Design Philosophy

LLMK follows several fundamental principles.

### LLM First

Language features are evaluated primarily from the perspective of whether they reduce misunderstanding by LLMs.

### Simplicity

A language feature should have exactly one purpose.

Complex syntax that combines multiple concepts is avoided.

### Deterministic Behavior

The behavior of every language feature should be uniquely determined from the source code.

Implicit or implementation-defined behavior is minimized.

### Function-Oriented Design

Functions are the smallest unit of behavior.

Complex logic should be expressed by composing small functions rather than by deeply nested control structures.

### Composition over Inheritance

Inheritance introduces hidden relationships that increase the complexity of software understanding.

LLMK therefore adopts composition instead of inheritance.

### One Concept per File

Each source file represents exactly one concept.

This improves discoverability for both humans and AI.

---

## 1.4 Non-goals

LLMK intentionally does not attempt to support every programming paradigm.

The following features are intentionally excluded.

- Class inheritance
- Multiple inheritance
- Else-if chains
- Early return
- Break
- Continue
- Complex nested expressions
- Deep control-flow nesting

These features are omitted to improve readability and reduce ambiguity.

---

## 1.5 Design Priorities

When a trade-off exists, LLMK prioritizes the following order.

1. Correct interpretation by LLMs
2. Readability for humans
3. Simplicity of language specification
4. Token efficiency
5. Runtime performance


# 2. Lexical Structure

## 2.1 Source File

The basic unit of a program is a source file.

Each source file shall represent exactly one concept.

The filename defines the module name.

Example

```
User.llmk
```

defines the module

```
User
```

No explicit module declaration is required.

---

## 2.2 Character Encoding

Source files shall be encoded using UTF-8.

---

## 2.3 Line Structure

LLMK is a line-oriented language.

Each statement occupies exactly one logical line.

A statement shall not span multiple lines except where explicitly allowed by the language specification.

---

## 2.4 Comments

Single-line comments begin with

```
//
```

Everything following `//` until the end of the line is ignored.

Example

```
// Create user
LET User user = User()
```

Multi-line comments are not supported.

---

## 2.5 Whitespace

Whitespace is used only to separate lexical elements.

Multiple spaces are treated as a single separator.

Indentation improves readability but does not define program semantics unless explicitly specified.

---

## 2.6 Identifiers

Identifiers consist of

- Unicode letters
- Digits
- Underscore (_)

The first character shall not be a digit.

Identifiers are case-sensitive.

Examples

```
User
user
user_name
Login
```

---

## 2.7 Keywords

The following words are reserved.

```
IMPORT

TYPE

FUNCTION

LET
VAR
REF

IF
MATCH
FOR
PARFOR

TRUE
FALSE
NONE

ERROR
```

Reserved keywords shall not be used as identifiers.

---

## 2.8 Parentheses

Parentheses are permitted for

- Function calls
- Instance creation

Examples

```
Save(user)

User()

User("Alice", 20)
```

Nested function calls are not permitted.

Valid

```
LET User user = Parse(text)
Save(user)
```

Invalid

```
Save(Parse(text))
```

---

## 2.9 Semicolons

Semicolons are not used.

Each statement ends at the end of the logical line.

---

## 2.10 Language Philosophy

The lexical structure of LLMK intentionally minimizes symbols and punctuation.

Every syntax element should have a single, unambiguous meaning.

Reducing ambiguity is prioritized over minimizing the number of characters.


# 3. Program Structure

## 3.1 Project Structure

A LLMK project consists of one or more source files.

Each source file defines exactly one module.

The module name is derived from the filename.

Example

```
User.llmk
Order.llmk
Math.llmk
```

defines the modules

```
User
Order
Math
```

---

## 3.2 One Concept per File

Each source file shall represent exactly one concept.

A concept may be

- a TYPE
- a module consisting of related functions

A source file shall not contain multiple unrelated concepts.

This rule improves readability and allows both humans and LLMs to understand the purpose of a file without additional context.

---

## 3.3 Module

A module is the namespace represented by a source file.

Modules do not require explicit declarations.

The module name is always identical to the filename.

Example

```
Math.llmk
```

```
FUNCTION Sqrt(...)
FUNCTION Pow(...)
```

Functions are referenced as

```
Math.Sqrt(...)
Math.Pow(...)
```

Global functions are not supported.

---

## 3.4 TYPE

A source file may define one TYPE.

If a TYPE is defined, all of the following rules apply.

- The TYPE name shall be identical to the module name.
- The TYPE name shall be identical to the filename.
- A source file shall contain at most one TYPE definition.

Example

```
User.llmk
```

```
TYPE User

    STRING name
    INT age
```

The following is invalid.

```
User.llmk

TYPE Customer
```

The following is also invalid.

```
User.llmk

TYPE User

TYPE Address
```

These restrictions ensure that every TYPE can be uniquely identified by its filename.

---

## 3.5 Function Modules

If a source file does not define a TYPE, it becomes a function module.

Example

```
Math.llmk
```

```
FUNCTION Sqrt(...)
FUNCTION Pow(...)
```

Functions are referenced using the module name.

```
Math.Sqrt(...)
Math.Pow(...)
```

---

## 3.6 IMPORT

Modules are imported using the IMPORT statement.

Example

```
IMPORT User
IMPORT Math
```

Imported modules are referenced by their module names.

```
LET User user = User()

LET DOUBLE result = Math.Sqrt(value)
```

---

## 3.7 Module Dependencies

Circular module dependencies should be avoided.

Language implementations may reject circular imports.

---

## 3.8 Design Principles

The program structure of LLMK follows these principles.

- One file represents one concept.
- One file defines one module.
- One file defines at most one TYPE.
- TYPE name, module name, and filename are always identical.
- Global namespaces are not supported.
- Explicit module declarations are unnecessary.


# 4. Type System

## 4.1 Overview

LLMK is a statically typed language.

The type of every variable, parameter, field, and function return value shall be explicitly declared.

Implicit type inference is not supported.

---

## 4.2 Built-in Literals

LLMK provides the following built-in literals.

| Literal | Description |
|----------|-------------|
| TRUE | Boolean true |
| FALSE | Boolean false |
| NONE | Absence of a meaningful value |

---

## 4.3 Primitive Types

LLMK provides the following primitive types.

| Type | Description |
|------|-------------|
| BOOL | Boolean value |
| INT | Signed integer |
| DOUBLE | Double-precision floating-point number |
| STRING | Unicode string |

Additional primitive types may be added by future language versions.

---

## 4.4 Composite Types

LLMK provides the following composite types.

```
ARRAY ! T
OPTIONAL ! T
```

Examples

```
ARRAY ! STRING

OPTIONAL ! User
```

Composite types may be nested.

Example

```
ARRAY ! OPTIONAL ! User
```

---

## 4.5 TYPE

TYPE defines a user-defined value type.

Example

```
TYPE User

    STRING name
    INT age
```

A TYPE groups related data into a single logical unit.

TYPEs do not support inheritance.

Composition is the preferred design approach.

---

## 4.6 Default Values

Every type has a well-defined default value.

Variables and fields are always initialized.

The default values are defined as follows.

| Type | Default Value |
|------|---------------|
| BOOL | FALSE |
| INT | 0 |
| DOUBLE | 0.0 |
| STRING | "" |
| ARRAY ! T | Empty array |
| OPTIONAL ! T | NONE |
| TYPE | Every field initialized to its default value |

Uninitialized values do not exist in LLMK.

---

## 4.7 NONE

`NONE` represents the absence of a meaningful value.

`NONE` is a built-in literal provided by the language.

`NONE` is used in the following situations.

- The default value of `OPTIONAL ! T`
- The return value of functions that do not produce a meaningful value

LLMK does not provide separate concepts such as `NULL`, `NIL`, `VOID`, or `UNIT`.

The language uses `NONE` as the single representation of the absence of a meaningful value.

---

## 4.8 Type Construction

Instances of a TYPE are created using the type construction expression.

The syntax is

```
TypeName()

TypeName(value1, value2, ...)
```

Type construction is a language construct.

It is not a function call and cannot be overridden.

If no arguments are specified, every field is initialized to its default value.

Example

```
TYPE User

    STRING name
    INT age
```

```
LET User user = User()
```

is equivalent to

```
name = ""
age = 0
```

If arguments are specified, they shall be assigned to the fields in declaration order.

Example

```
LET User user = User(
    "Alice",
    20
)
```

is equivalent to

```
name = "Alice"
age = 20
```

The number of arguments shall exactly match the number of fields.

Named arguments are not supported.

User-defined constructors are not supported.

---
## 4.9 Value Semantics

All values are copied by default.

Assignment creates an independent copy.

Example

```
LET User user1 = User()

LET User user2 = user1
```

Modifying `user2` does not affect `user1`.

Reference semantics require the explicit use of `REF`.

---

## 4.10 Reference Semantics

LLMK uses value semantics by default.

Reference semantics are only available through `REF`.

Implicit reference sharing is not supported.

The detailed behavior of `REF` is defined in a later chapter.

---

## 4.11 Type Conversion

Implicit type conversion is not supported.

All type conversions shall be explicit.

Example

```
INT(value)

DOUBLE(value)

STRING(value)
```

---

## 4.12 Equality

Primitive types support value equality.

TYPE equality compares every field.

Composite types compare their contained values recursively.

---

## 4.13 Design Principles

The type system follows these principles.

- Every value has exactly one type.
- Every type has a deterministic default value.
- Every variable and field is initialized.
- Value semantics are the default.
- Reference semantics require explicit `REF`.
- Composition is preferred over inheritance.

---

# 5. Variables

## 5.1 Overview

Variables store values.

Every variable has exactly one type.

The type of every variable shall be explicitly declared.

Variables are declared using either `LET` or `VAR`.

---

## 5.2 LET

`LET` declares an immutable variable binding.

A `LET` variable shall be initialized when declared.

Example

```
LET INT count = 0

LET STRING name = "Alice"

LET User user = User()
```

A `LET` variable cannot be assigned another value after initialization.

Example

```
LET INT count = 0

count = 1      // Invalid
```

When the value is a TYPE, `LET` prevents reassignment of the variable itself.

The fields of the TYPE remain mutable.

Example

```
LET User user = User()

user.name = "Alice"      // Valid

user = User()            // Invalid
```

---

## 5.3 VAR

`VAR` declares a mutable variable binding.

A `VAR` variable shall be initialized when declared.

Example

```
VAR INT count = 0

count = 1
```

TYPE variables may also be reassigned.

Example

```
VAR User user = User()

user = User()
```

---

## 5.4 Initialization

Every variable shall be initialized at the point of declaration.

Uninitialized variables are not supported.

Valid

```
LET INT count = 0

VAR User user = User()
```

Invalid

```
LET INT count

VAR User user
```

---

## 5.5 Assignment

Assignment replaces the current value of a mutable variable.

Assignments to `LET` variables are not permitted.

Assignment copies the value.

Reference semantics are not used unless explicitly specified by the language.

Example

```
VAR INT count = 0

count = 10
```

---

## 5.6 Scope

Variables are visible only within the scope in which they are declared.

Variables declared inside a function are local to that function.

Shadowing should be avoided.

Language implementations may reject duplicate declarations within the same scope.

---

## 5.7 Design Principles

The variable model follows these principles.

- Every variable has exactly one type.
- Every variable is initialized.
- Variables are declared using either `LET` or `VAR`.
- `LET` defines an immutable variable binding.
- `VAR` defines a mutable variable binding.
- TYPE fields remain mutable.
- Assignment copies values by default.


---

# 6. Functions

## 6.1 Overview

Functions define program behavior.

Functions are the smallest unit of executable logic in LLMK.

Complex behavior should be expressed by composing small functions rather than by deeply nested control structures.

---

## 6.2 Function Declaration

Functions are declared using the `FUNCTION` keyword.

Example

```
FUNCTION PrintUser(

    User user
)
```

Function names shall be unique within a module.

If a module defines a TYPE, every function in the module belongs to that TYPE.

---

## 6.3 Parameters

Every parameter shall have an explicitly declared type.

Parameters are passed by value unless declared with `REF`.

Named arguments are not supported.

Arguments are matched by position.

Example

```
FUNCTION Print(

    User user
)
```

---

## 6.4 REF Parameters

`REF` declares a parameter that is passed by reference.

Example

```
FUNCTION Rename(

    REF User user

    STRING name
)
```

A function with a `REF` parameter may modify the caller's value.

`REF` may only be used for function parameters.

Reference variables are not supported.

---

## 6.5 Return Values

Every function returns exactly one value.

The final executable statement of a function shall produce the return value.

The `RETURN` statement is not supported.

Every function shall terminate with a statement that produces a value.

Functions that do not produce a meaningful value shall terminate with the literal `NONE`.

---

## 6.6 Function Calls

Functions are called using parentheses.

Example

```
Save(user)

Print(name)
```

Arguments are evaluated before the function is executed.

Nested function calls are not supported.

Valid

```
LET User user = Parse(text)

Save(user)
```

Invalid

```
Save(Parse(text))
```

---

## 6.7 Functions in TYPE Modules

When a module defines a TYPE, every function in the module belongs to that TYPE.

Example

```
User.llmk

TYPE User

    STRING name

FUNCTION Rename(

    REF User user

    STRING name
)

FUNCTION Validate(

    User user
)
```

The functions `Rename` and `Validate` belong to the `User` TYPE.

No separate method declaration syntax exists.

The language does not define concepts such as methods, member functions, `this`, or `self`.

---

## 6.8 Function Composition

Functions should perform one logical task.

Larger operations should be composed from smaller functions.

Example

```
ValidateUser(user)

SaveUser(user)

NotifyUser(user)
```

instead of one large function.

---

## 6.9 Design Principles

The function model follows these principles.

- Functions are the smallest unit of behavior.
- Parameters are passed by value by default.
- `REF` explicitly declares mutable parameters.
- `RETURN` is not supported.
- Function calls shall not be nested.
- Large functions should be divided into smaller functions.
- Functions belonging to a TYPE are determined by their module.

