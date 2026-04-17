"""Codegen for single functions."""
from __future__ import annotations
import ast
import sys
from latexify import ast_utils, exceptions
from latexify.codegen import codegen_utils, expression_codegen, identifier_converter

class FunctionCodegen(ast.NodeVisitor):
    """Codegen for single functions.

    This codegen works for Module with single FunctionDef node to generate a single
    LaTeX expression of the given function.
    """
    _identifier_converter: identifier_converter.IdentifierConverter
    _use_signature: bool

    def __init__(self, *, use_math_symbols: bool=False, use_signature: bool=True, use_set_symbols: bool=False, escape_underscores: bool=True) -> None:
        """Initializer.

        Args:
            use_math_symbols: Whether to convert identifiers with a math symbol surface
                (e.g., "alpha") to the LaTeX symbol (e.g., "\\alpha").
            use_signature: Whether to add the function signature before the expression
                or not.
            use_set_symbols: Whether to use set symbols or not.
        """
        self._expression_codegen = expression_codegen.ExpressionCodegen(use_math_symbols=use_math_symbols, use_set_symbols=use_set_symbols, escape_underscores=escape_underscores)
        self._identifier_converter = identifier_converter.IdentifierConverter(use_math_symbols=use_math_symbols, escape_underscores=escape_underscores)
        self._use_signature = use_signature

    def generic_visit(self, node: ast.AST) -> str:
        pass

    def visit_Module(self, node: ast.Module) -> str:
        """Visit a Module node."""
        pass

    def visit_FunctionDef(self, node: ast.FunctionDef) -> str:
        """Visit a FunctionDef node."""
        pass

    def visit_Assign(self, node: ast.Assign) -> str:
        """Visit an Assign node."""
        pass

    def visit_Return(self, node: ast.Return) -> str:
        """Visit a Return node."""
        pass

    def visit_If(self, node: ast.If) -> str:
        """Visit an If node."""
        pass

    def visit_Match(self, node: ast.Match) -> str:
        """Visit a Match node"""
        pass

    def visit_MatchValue(self, node: ast.MatchValue) -> str:
        """Visit a MatchValue node"""
        pass
