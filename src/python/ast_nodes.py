"""AST node definitions for ai-kaizen-lang."""

from dataclasses import dataclass
from typing import List, Optional, Any
from enum import Enum, auto


class ASTNode:
    """Base class for all AST nodes."""
    pass


class Type(ASTNode):
    """Base class for type nodes."""
    pass


@dataclass
class PrimitiveType(Type):
    """Primitive type: INT, STRING, or BOOL."""
    name: str


@dataclass
class ArrayType(Type):
    """Array type: ARRAY ! TYPE."""
    element_type: Type


@dataclass
class StructType(Type):
    """Struct type."""
    name: str


@dataclass
class RefType(Type):
    """Reference type: REF TYPE."""
    inner_type: Type


@dataclass
class TaskType(Type):
    """Task type: TASK TYPE."""
    result_type: Type


# Value and Expression nodes

@dataclass
class IntLiteral(ASTNode):
    """Integer literal."""
    value: int


@dataclass
class StringLiteral(ASTNode):
    """String literal."""
    value: str


@dataclass
class BoolLiteral(ASTNode):
    """Boolean literal."""
    value: bool


@dataclass
class Identifier(ASTNode):
    """Variable or function identifier."""
    name: str


@dataclass
class BinaryOp(ASTNode):
    """Binary operation: value OP value."""
    left: ASTNode
    operator: str
    right: ASTNode


@dataclass
class FunctionCall(ASTNode):
    """Function call."""
    name: str
    arguments: List[ASTNode]


@dataclass
class StructInit(ASTNode):
    """Struct initialization."""
    struct_type: str
    fields: List[ASTNode]


@dataclass
class ArrayInit(ASTNode):
    """Array initialization."""
    elements: List[ASTNode]


# Statement nodes

@dataclass
class LetStatement(ASTNode):
    """Let (immutable) variable declaration."""
    name: str
    var_type: Type
    value: ASTNode


@dataclass
class VarStatement(ASTNode):
    """Var (mutable) variable declaration."""
    name: str
    var_type: Type
    value: ASTNode


@dataclass
class AssignmentStatement(ASTNode):
    """Variable assignment."""
    name: str
    value: ASTNode


@dataclass
class IfStatement(ASTNode):
    """If statement."""
    condition: ASTNode
    then_block: List[ASTNode]
    else_block: Optional[List[ASTNode]]


@dataclass
class ForStatement(ASTNode):
    """For loop statement."""
    array: ASTNode
    item_name: str
    body: List[ASTNode]


@dataclass
class ReturnStatement(ASTNode):
    """Return statement."""
    value: ASTNode


@dataclass
class FunctionDef(ASTNode):
    """Function definition."""
    return_type: Type
    name: str
    parameters: List[tuple]  # [(name, type), ...]
    body: List[ASTNode]
    is_error_func: bool = False
    error_handler: Optional[List[ASTNode]] = None


@dataclass
class StructDef(ASTNode):
    """Struct definition."""
    name: str
    fields: List[tuple]  # [(name, type), ...]


@dataclass
class ImportStatement(ASTNode):
    """Import statement."""
    module_path: str
    alias: Optional[str]


@dataclass
class Program(ASTNode):
    """Root node representing the entire program."""
    statements: List[ASTNode]
