"""Unit tests for the lexer."""

import pytest
from src.python.lexer import Lexer, TokenType


class TestLexer:
    """Test cases for lexer functionality."""
    
    def test_empty_input(self):
        """Test lexing empty input."""
        lexer = Lexer("")
        tokens = lexer.tokenize()
        assert len(tokens) == 1
        assert tokens[0].type == TokenType.EOF
    
    def test_simple_integer(self):
        """Test lexing a simple integer."""
        lexer = Lexer("42")
        tokens = lexer.tokenize()
        assert tokens[0].type == TokenType.INT_LITERAL
        assert tokens[0].value == "42"
    
    def test_string_literal(self):
        """Test lexing a string literal."""
        lexer = Lexer('"hello world"')
        tokens = lexer.tokenize()
        assert tokens[0].type == TokenType.STRING_LITERAL
        assert tokens[0].value == "hello world"
    
    def test_keywords(self):
        """Test lexing reserved keywords."""
        lexer = Lexer("LET VAR INT STRING BOOL FUNC RETURN")
        tokens = lexer.tokenize()
        expected_types = [
            TokenType.LET, TokenType.VAR, TokenType.INT, TokenType.STRING,
            TokenType.BOOL, TokenType.FUNC, TokenType.RETURN
        ]
        for token, expected_type in zip(tokens, expected_types):
            assert token.type == expected_type
    
    def test_operators(self):
        """Test lexing operators."""
        lexer = Lexer("+ - * / == !=  && ||")
        tokens = lexer.tokenize()
        expected_types = [
            TokenType.PLUS, TokenType.MINUS, TokenType.MULTIPLY,
            TokenType.DIVIDE, TokenType.EQ, TokenType.NE,
            TokenType.AND, TokenType.OR
        ]
        for token, expected_type in zip(tokens, expected_types):
            assert token.type == expected_type
    
    def test_comments(self):
        """Test that comments are skipped."""
        lexer = Lexer("LET x = 42 # This is a comment")
        tokens = lexer.tokenize()
        # Comment should be skipped
        assert tokens[0].type == TokenType.LET
