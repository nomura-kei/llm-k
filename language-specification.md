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

---

## 3.8 Program Execution

LLMK does not define a reserved entry function.

The execution environment specifies the module and function to execute.

---

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

---

# 7. Control Flow

## 7.1 Overview

LLMK control flow is designed to minimize nesting and ambiguity.

Control structures do not contain arbitrary statements.

Control structures only select or invoke functions.

Complex behavior shall be expressed by composing functions.

---

## 7.2 IF

`IF` executes a function when a boolean condition is true.

Syntax

```
IF condition

    Function()
```

The condition shall be a BOOL value.

The condition shall not contain expressions.

Example

```
IF isSuccess

    Execute()
```

`IF` does not provide an `ELSE` clause.

Alternative behavior shall be expressed using another condition.

Example

```
IF isSuccess

    ExecuteSuccess()

IF isFailed

    ExecuteFailure()
```

---

## 7.3 MATCH

`MATCH` selects a function based on the value of a variable.

Syntax

```
MATCH variable

    value Function()
```

Example

```
MATCH status

    SUCCESS HandleSuccess()

    FAILED HandleFailure()
```

`MATCH` does not execute arbitrary statements.

Each branch shall call exactly one function.

---

## 7.4 FOR

`FOR` applies a function to every element of an array.

Elements are processed in array order.

Syntax

```
FOR array Function()
```

Example

```
FOR users SendNotification()
```

The function receives one element at a time.

The execution order is guaranteed.

The result values are collected in an array when the function returns a value.

---

## 7.5 PARFOR

`PARFOR` applies a function to every element of an array in parallel.

All elements shall be processed.

Execution order is not guaranteed.

The caller waits until all executions complete.

Syntax

```
PARFOR array Function()
```

Example

```
PARFOR users SendNotification()
```

---

## 7.6 PARFOR Results

When the executed function returns values, `PARFOR` returns an array containing all results.

The result array order is identical to the input array order.

Example

```
LET ARRAY ! Result results = PARFOR users ProcessUser()
```

Even though execution is parallel, result ordering is deterministic.

---

## 7.7 PARFOR Error Handling

If an execution fails, `PARFOR` does not stop remaining executions.

All elements are processed.

The final result contains the result of every execution.

Failure handling is defined by the Error Handling specification.

---

## 7.8 REF Restriction

Functions called by `PARFOR` shall not contain `REF` parameters.

Parallel execution cannot modify shared mutable state.

Example

Invalid

```
PARFOR users UpdateUser()
```

when

```
FUNCTION UpdateUser(

    REF User user
)
```

exists.

---

## 7.9 Design Principles

The control flow model follows these principles.

- Conditions contain only BOOL values.
- Control structures only invoke functions.
- ELSE is not supported.
- RETURN-based early exits are not supported.
- FOR preserves order.
- PARFOR provides parallel execution with deterministic results.
- Shared mutable state is avoided.

---

# 8. Error Handling

## 8.1 Overview

LLMK treats errors as explicit values.

Errors are not hidden control flows.

A function that may fail shall explicitly define its error behavior.

The caller shall be able to understand possible failures by reading the function interface.

---

## 8.2 RESULT Type

LLMK provides the built-in generic type `RESULT`.

`RESULT` represents either a successful value or an error value.

Syntax

```
RESULT ! T
```

Example

```
RESULT ! User
```

represents either:

* a successful `User` value
* an error value

---

## 8.3 SUCCESS and ERROR Values

A `RESULT ! T` value contains exactly one of the following states.

```
SUCCESS(value)

ERROR(error)
```

Example

```
SUCCESS(user)

ERROR(NotFound)
```

---

## 8.4 Error Declaration

A function that may fail shall declare possible error types.

Example

```
FUNCTION LoadUser(

    INT id
)

ERROR

    NotFound
    PermissionDenied
```

The declared errors are part of the function contract.

---

## 8.5 Function Return Type

Functions that may fail shall return a `RESULT ! T` type.

Example

```
FUNCTION LoadUser(

    INT id
)

RESULT ! User

ERROR

    NotFound
```

A successful execution returns:

```
SUCCESS(user)
```

A failed execution returns:

```
ERROR(NotFound)
```

---

## 8.6 Error Handling with MATCH

Errors shall be handled explicitly.

`MATCH` is used to select handling functions.

Example

```
MATCH result

    SUCCESS HandleUser()

    ERROR HandleError()
```

Error handling shall not be implicit.

---

## 8.7 Error Propagation

A function calling another function that returns `RESULT` shall explicitly handle or propagate the result.

Implicit error propagation is not supported.

---

## 8.8 PARFOR Error Handling

`PARFOR` executes all elements regardless of individual failures.

A failure in one execution shall not interrupt remaining executions.

All execution results are returned after completion.

Example

```
PARFOR users ProcessUser()
```

Possible result:

```
[
    SUCCESS(user1),
    ERROR(NotFound),
    SUCCESS(user3)
]
```

The result order is identical to the input array order.

---

## 8.9 Design Principles

The error handling model follows these principles.

* Errors are values.
* Failure states are explicit.
* Functions declare possible errors.
* Hidden exception flows are avoided.
* MATCH handles success and error states.
* PARFOR completes all executions before returning results.

---

# 9. Built-in Types and Standard Library

## 9.1 Overview

LLMK separates language features from the standard library.

Language built-in features are defined by the language specification.

Standard library features are provided as modules and may evolve independently from the language specification.

---

## 9.2 Built-in Types

The following types are built into LLMK.

| Type         | Description                           |
| ------------ | ------------------------------------- |
| BOOL         | Boolean value                         |
| INT          | Integer value                         |
| DOUBLE       | Double-precision floating-point value |
| STRING       | Unicode string                        |
| ARRAY ! T    | Ordered collection of values          |
| OPTIONAL ! T | Optional value                        |
| RESULT ! T   | Success or error value                |

Built-in types are always available.

No import is required.

---

## 9.3 Built-in Literals

The following literals are built into LLMK.

| Literal | Description                   |
| ------- | ----------------------------- |
| TRUE    | Boolean true value            |
| FALSE   | Boolean false value           |
| NONE    | Absence of a meaningful value |

`NONE` is used as the empty state of `OPTIONAL` and as a return value when a function has no meaningful result.

---

## 9.4 ARRAY

`ARRAY ! T` represents an ordered collection.

The order of elements is always preserved.

Example

```
ARRAY ! STRING
```

ARRAY supports:

* Iteration by `FOR`
* Parallel processing by `PARFOR`

The detailed operations of ARRAY are defined by the standard library.

---

## 9.5 OPTIONAL

`OPTIONAL ! T` represents a value that may not exist.

Example

```
OPTIONAL ! User
```

Possible states:

```
User value

NONE
```

`OPTIONAL` represents absence of a value.

It does not represent an error.

---

## 9.6 RESULT

`RESULT ! T` represents the result of an operation that may succeed or fail.

Possible states:

```
SUCCESS(value)

ERROR(error)
```

`RESULT` is used when an operation may not complete successfully.

It does not represent absence of a value.

---

## 9.7 Standard Library

The standard library provides commonly used functionality as modules.

Standard library modules follow normal LLMK module rules.

Example

```
IMPORT File
IMPORT Json
IMPORT Math
```

Standard library modules:

* Use the same syntax as user-defined modules.
* Do not require special language syntax.
* May be extended independently.

---

## 9.8 Language Feature and Library Boundary

A feature shall be part of the language specification only when it affects program structure or interpretation.

Examples of language features:

* Variables
* Functions
* TYPE
* Control flow
* Built-in types

Examples of standard library features:

* File access
* Network communication
* Data formats
* Time operations
* External services

---

## 9.9 Design Principles

The built-in type and library model follows these principles.

* The language core remains small.
* Common functionality is provided through modules.
* Built-in features have deterministic behavior.
* Library features follow normal module rules.
* The distinction between syntax and library functionality is explicit.


---

# 10. Recommended Coding Style

## 10.1 Overview

This chapter defines recommended coding practices for LLMK programs.

These rules are not required by the language specification.

They are intended to improve readability, maintainability, and accuracy of AI-assisted software development.

---

## 10.2 One Concept per File

Each source file should represent one concept.

A module should have a clear and limited responsibility.

Example:

```
User.llmk
Order.llmk
Payment.llmk
```

Avoid placing unrelated functionality in the same file.

The purpose of a file should be understandable from its filename.

---

## 10.3 Small Functions

Functions should perform one logical task.

Large functions should be divided into smaller functions.

Example:

```
ValidateUser(user)

SaveUser(user)

NotifyUser(user)
```

Avoid functions that perform many unrelated operations.

Small functions improve:

- Human readability
- LLM understanding
- Testing
- Code reuse

---

## 10.4 Function Parameter Count

Functions should have three or fewer parameters.

Example:

```
FUNCTION CreateUser(

    STRING name

    INT age

    STRING email
)
```

When a function requires more parameters, consider creating a TYPE.

Example:

```
TYPE UserCreateRequest

    STRING name
    INT age
    STRING email
    STRING address
```

Then pass the TYPE instead.

```
FUNCTION CreateUser(

    UserCreateRequest request
)
```

---

## 10.5 Prefer TYPE for Related Data

Related values should be grouped into a TYPE.

Avoid:

```
FUNCTION CreateOrder(

    STRING userName

    STRING address

    STRING productName

    INT quantity
)
```

Prefer:

```
TYPE OrderRequest

    User user
    Product product
    INT quantity
```

Grouping related data into TYPE improves semantic clarity.

---

## 10.6 Avoid Deep Nesting

Control structures should not be deeply nested.

LLMK control structures only call functions.

Avoid:

```
IF conditionA

    IF conditionB

        Execute()
```

Prefer:

```
IF conditionA

    CheckConditionB()
```

Complex conditions should be moved into functions.

---

## 10.7 Boolean Naming

Boolean variables and functions should clearly represent a state or condition.

Recommended prefixes:

```
is
has
can
should
```

Examples:

```
isActive

hasPermission

canExecute
```

Boolean names should describe a condition rather than an action.

---

## 10.8 Function Naming

Function names should represent actions.

Recommended:

```
CreateUser()

ValidateOrder()

SendMessage()
```

Avoid vague names:

```
Process()

Handle()

DoSomething()
```

---

## 10.9 TYPE Naming

TYPE names should represent entities or concepts.

Recommended:

```
User

Order

PaymentRequest
```

Avoid implementation-specific names:

```
UserData

TempObject

Manager
```

---

## 10.10 Avoid Unnecessary Abstraction

LLMK favors explicit and simple designs.

Avoid creating abstractions only for possible future requirements.

Code should represent current requirements clearly.

Unnecessary abstraction increases the amount of information that both humans and LLMs must understand.

---

## 10.11 Explicit over Clever

LLMK code should prefer explicit behavior over compact or clever implementations.

Avoid:

- Hidden side effects
- Complex expressions
- Unclear naming
- Excessive abstraction

Prefer:

- Small functions
- Clear names
- Simple control flow
- Explicit data flow

---

## 10.12 Design Principles

The recommended coding style follows these principles.

- Optimize for LLM readability.
- Keep responsibilities clear.
- Prefer composition over complexity.
- Use TYPE to represent concepts.
- Use functions to represent behavior.
- Minimize hidden behavior.
- Prefer explicit code over clever code.


---



# 11. Example Programs

## 11.1 Overview

This chapter provides example LLMK programs.

These examples demonstrate recommended usage of LLMK features.

The examples are not part of the language specification.

---

## 11.2 Program Entry Point

LLMK does not define a special entry point such as `Main`.

Any function may be used as the program entry point.

The execution environment specifies the module and function to execute.

Example:

```
llmk run Application Start
```

This executes:

```
Application.llmk

FUNCTION Start()
```

No function name is reserved for program startup.

---

## 11.3 Hello World

Example:

```
FUNCTION Start()

    Print("Hello World")
```

The execution environment may execute `Start` as the entry point.

---

## 11.4 TYPE and Module Example

A file defines one module.

The filename, module name, and TYPE name are identical.

Example file:

```
User.llmk
```

Content:

```
TYPE User

    STRING name
    STRING email


FUNCTION Create(

    STRING name

)

    User(
        name,
        ""
    )


FUNCTION Validate(

    User user

)

    ValidateUser(user)
```

All functions in `User.llmk` belong to the `User` TYPE.

No separate method declaration syntax exists.

---

## 11.5 Immutable and Mutable Variables

Example:

```
LET STRING name = "Alice"

VAR INT count = 0

count = 1
```

`LET` prevents reassignment.

`VAR` allows reassignment.

---

## 11.6 IF Example

Conditions are BOOL values.

Control structures only call functions.

Example:

```
LET BOOL isValid = Validate(user)

IF isValid

    SaveUser(user)
```

Alternative behavior is expressed using another condition.

Example:

```
LET BOOL isInvalid = NotValidate(user)

IF isInvalid

    RejectUser(user)
```

---

## 11.7 MATCH Example

MATCH selects a function based on a value.

Example:

```
LET RESULT ! User result = LoadUser(id)

MATCH result

    SUCCESS UseUser()

    ERROR HandleError()
```

---

## 11.8 FOR Example

FOR processes elements sequentially.

Example:

```
FOR users SendNotification()
```

The execution order follows the array order.

---

## 11.9 PARFOR Example

PARFOR processes elements in parallel.

Example:

```
LET ARRAY ! RESULT ! User results = PARFOR users ProcessUser()
```

All elements are processed.

The result order matches the input array order.

---

## 11.10 REF Example

REF explicitly allows modification.

Example:

```
FUNCTION Rename(

    REF User user

    STRING name
)

    user.name = name

    NONE
```

Without REF, values are passed by value.

---

## 11.11 Function Composition Example

Large operations should be divided into small functions.

Avoid:

```
ProcessEverything()
```

Prefer:

```
ValidateOrder(order)

CalculatePrice(order)

SaveOrder(order)

NotifyCustomer(order)
```

---

## 11.12 Design Principles Demonstrated

These examples demonstrate the following LLMK principles.

- Explicit behavior
- Small functions
- Limited control flow
- Visible data modification
- Clear error handling
- Simple module structure
- No unnecessary special cases

---

# 12. Formal Grammar

## 12.1 Overview

This chapter defines the formal structure of LLMK syntax.

The grammar describes the relationship between modules, types, functions, variables, and control structures.

This grammar is intended as a reference for language implementations.

---

## 12.2 Program Structure

A program consists of one or more modules.

```
program ::= module+
```

A module is defined by one source file.

```
module ::= type_definition function_definition*
```

A module name is identical to the filename.

---

## 12.3 TYPE Definition

A TYPE defines a data structure.

```
type_definition ::=
    TYPE identifier
        field_definition*
```

A TYPE contains fields.

```
field_definition ::=
    type identifier
```

A module may define at most one TYPE.

The TYPE name shall be identical to the module name.

---

## 12.4 Function Definition

A function defines executable behavior.

```
function_definition ::=
    FUNCTION identifier
        parameter_list
        statement*
```

Parameters are defined by type and name.

```
parameter ::=
    REF? type identifier
```

---

## 12.5 Variable Declaration

Variables are declared using LET or VAR.

```
variable_declaration ::=
    LET type identifier = value
    |
    VAR type identifier = value
```

Every variable shall be initialized.

---

## 12.6 Function Call

A function call invokes a function.

```
function_call ::=
    identifier(arguments)
```

Arguments are passed by position.

Named arguments are not supported.

Nested function calls are not supported.

---

## 12.7 IF

IF executes a function when a BOOL value is true.

```
if_statement ::=
    IF bool_identifier
        function_call
```

The condition shall be a BOOL value.

---

## 12.8 MATCH

MATCH selects a function based on a value.

```
match_statement ::=
    MATCH identifier
        match_case+
```

A match case consists of a value and a function call.

```
match_case ::=
    value function_call
```

---

## 12.9 FOR

FOR applies a function to every array element.

```
for_statement ::=
    FOR array_identifier function_call
```

Execution order follows array order.

---

## 12.10 PARFOR

PARFOR applies a function to every array element in parallel.

```
parfor_statement ::=
    PARFOR array_identifier function_call
```

All executions complete before returning results.

---

## 12.11 Return Value

A function returns the value produced by the final executable statement.

```
function_return ::=
    final_statement
```

Every function shall end with a statement producing a value.

The RETURN statement does not exist.

---

## 12.12 Error Declaration

Functions may declare possible errors.

```
error_definition ::=
    ERROR
        error_type*
```

A function returning possible errors shall return:

```
RESULT ! T
```

---

## 12.13 Type Expressions

Type expressions are defined as:

```
type ::=
    primitive_type
    |
    TYPE_NAME
    |
    ARRAY ! type
    |
    OPTIONAL ! type
    |
    RESULT ! type
```

---

## 12.14 Design Principles

The formal grammar follows these principles.

- Syntax is explicit.
- Ambiguous constructs are avoided.
- Control structures only call functions.
- Complex expressions are not supported.
- Program structure is determined by modules and functions.

---

# 13. Expression and Evaluation Rules

## 13.1 Overview

LLMK uses a simple evaluation model designed for predictable behavior.

Expressions are intentionally limited.

Complex expressions are not supported.

Program logic should be expressed through functions and explicit values.

---

## 13.2 Values

A value is a literal, variable, or function result.

Examples:

```
10

"Hello"

TRUE

user

GetUser()
```

Values have exactly one type.

---

## 13.3 No Complex Expressions

LLMK does not support complex expressions.

The following are not supported:

```
a + b * c

user.age > 20

isActive && hasPermission

condition ? value1 : value2
```

Complex logic shall be implemented by functions.

Example:

```
LET BOOL canAccess = CheckAccess(user)

IF canAccess

    AllowAccess()
```

---

## 13.4 Operators

Operators are intentionally limited.

LLMK does not provide general expression operators.

Operations shall be performed by functions.

Example:

Instead of:

```
total = price * quantity
```

Use:

```
LET INT total = CalculateTotal(price, quantity)
```

---

## 13.5 Function Evaluation

Function calls are evaluated before their result is used.

Example:

```
LET User user = LoadUser(id)
```

The function `LoadUser` is executed and the returned value is assigned.

Function calls shall not be nested.

Invalid:

```
SaveUser(ParseUser(data))
```

Valid:

```
LET User user = ParseUser(data)

SaveUser(user)
```

---

## 13.6 Assignment Evaluation

Assignment stores a value into a mutable variable.

Example:

```
VAR INT count = 0

count = GetCount()
```

The right side is evaluated first.

The result is then assigned.

---

## 13.7 Boolean Evaluation

Boolean values are explicit values.

Conditions require a BOOL value.

Example:

```
LET BOOL isReady = CheckReady()

IF isReady

    Start()
```

The following are not supported:

```
IF count > 0

IF user != NONE

IF a && b
```

Such logic shall be implemented by functions.

---

## 13.8 Evaluation Order

LLMK evaluation order is deterministic.

The order is:

1. Evaluate function arguments.
2. Execute the function.
3. Receive the result.
4. Assign or use the result.

Side effects occur only through explicitly defined mechanisms.

---

## 13.9 Side Effects

Side effects are only allowed through:

- Functions with `REF` parameters.
- External operations defined by standard library modules.

Functions without `REF` parameters should not modify external state.

---

## 13.10 Design Principles

The expression model follows these principles.

- Prefer functions over operators.
- Avoid implicit behavior.
- Keep evaluation deterministic.
- Make data flow visible.
- Minimize syntax ambiguity.
- Optimize for LLM understanding.

---

T.B.D.

以下、記載予定

14. Module System

※重要度高

内容:

ファイル = モジュール
TYPE名 = ファイル名 = モジュール名
import仕様
標準ライブラリとユーザーモジュールの扱い
循環参照禁止
モジュール間アクセス規則

現在3章・9章で一部触れていますが、独立章にした方が良いです。

15. Object System

※重要度高

内容:

TYPE
インスタンス生成
フィールドアクセス
継承なし
ポリモーフィズムなし
composition（組み合わせ）による設計

現在4章ではデータ型として扱っていますが、OOP部分は別章が必要です。

16. Memory and Reference Model

※重要度高

内容:

値渡しが基本
REFは関数引数のみ
REF可能なのはVARのみ
ローカル変数へのREF禁止
コピータイミング
ライフサイクル

以前議論したメモリモデルを正式化する章です。

17. Concurrency Model

※重要度高

内容:

PARFOR
並列実行モデル
実行順序保証
結果順序保証
REF禁止理由
将来のasync/spawn/join拡張余地

7章のPARFORだけでは不足しています。

18. Standard Library Specification

内容:

標準ライブラリ設計方針
Module形式
File
Network
JSON
DateTime
Math

9章の「扱い」から詳細へ分離。

19. Security and Safety Model

LLMKではAI生成コードを想定するため重要。

内容:

副作用の明示
外部アクセス制御
権限モデル
unsafe機能の扱い
秘密情報管理
20. Tool and AI Integration

LLMK固有として重要。

内容:

MCPなど外部ツール連携
AIが読むメタ情報
モジュール解析
コード生成時の補助情報
Tool呼び出し規約

LLMファースト言語として特徴になる部分です。

21. Versioning and Compatibility

内容:

言語バージョン
互換性
非互換変更
標準ライブラリバージョン
22. Future Extensions

将来検討事項。

候補:

Generic
Interface
Async
Package Manager
Reflection
Macro
AI Annotation
