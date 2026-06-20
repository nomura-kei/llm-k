#!/usr/bin/env python3
"""Command-line interface for ai-kaizen-lang."""

import sys
import argparse
from pathlib import Path
from .lexer import Lexer
from .parser import Parser
from .type_checker import TypeChecker
from .error_validator import ErrorValidator
from .parallel_validator import ParallelValidator
from .runtime import Runtime


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="ai-kaizen-lang (aikai) interpreter"
    )
    
    parser.add_argument(
        "file",
        type=str,
        help="Path to the .aikai file to run"
    )
    
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Only perform type checking, don't execute"
    )
    
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print verbose output"
    )
    
    args = parser.parse_args()
    
    # Read source file
    try:
        source = Path(args.file).read_text()
    except FileNotFoundError:
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        return 1
    
    # Lexical analysis
    if args.verbose:
        print("[*] Lexical analysis...")
    
    lexer = Lexer(source)
    try:
        tokens = lexer.tokenize()
    except Exception as e:
        print(f"Lexical error: {e}", file=sys.stderr)
        return 1
    
    if args.verbose:
        print(f"    Generated {len(tokens)} tokens")
    
    # Parsing
    if args.verbose:
        print("[*] Parsing...")
    
    parser_obj = Parser(tokens)
    try:
        ast = parser_obj.parse()
    except Exception as e:
        print(f"Parse error: {e}", file=sys.stderr)
        return 1
    
    if args.verbose:
        print(f"    AST generated")
    
    # Type checking
    if args.verbose:
        print("[*] Type checking...")
    
    type_checker = TypeChecker()
    if not type_checker.check(ast):
        for error in type_checker.get_errors():
            print(f"Type error: {error}", file=sys.stderr)
        return 1
    
    if args.verbose:
        print("    Type checking passed")
    
    # ERROR validation
    if args.verbose:
        print("[*] ERROR validation...")
    
    error_validator = ErrorValidator()
    if not error_validator.validate(ast):
        for error in error_validator.get_errors():
            print(f"ERROR validation error: {error}", file=sys.stderr)
        return 1
    
    if args.verbose:
        print("    ERROR validation passed")
    
    # Parallel constraint validation
    if args.verbose:
        print("[*] Parallel constraint validation...")
    
    parallel_validator = ParallelValidator()
    if not parallel_validator.validate(ast):
        for error in parallel_validator.get_errors():
            print(f"Parallel error: {error}", file=sys.stderr)
        return 1
    
    if args.verbose:
        print("    Parallel constraint validation passed")
    
    if args.check_only:
        if args.verbose:
            print("[+] All checks passed")
        return 0
    
    # Execution
    if args.verbose:
        print("[*] Execution...")
    
    runtime = Runtime()
    try:
        result = runtime.execute(ast)
    except Exception as e:
        print(f"Runtime error: {e}", file=sys.stderr)
        return 1
    
    if args.verbose:
        print("[+] Execution completed")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
