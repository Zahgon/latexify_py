"""Transformer to replace user symbols."""

from __future__ import annotations

import ast
import keyword
from typing import cast

from latexify import ast_utils


class IdentifierReplacer(ast.NodeTransformer):
    """NodeTransformer to replace identifier names.

    This class defines a rule to replace identifiers in AST with specified names.

    Example:
        def foo(bar):
            return baz

        IdentifierReplacer({"foo": "x", "bar": "y", "baz": "z"}) will modify the AST of
        the function above to below:

        def x(y):
            return z
    """

    def __init__(self, mapping: dict[str, str]):
        """Initializer.

        Args:
            mapping: User defined mapping of names. Keys are the original names of the
                identifiers, and corresponding values are the replacements.
                Both keys and values have to represent valid Python identifiers:
                ^[A-Za-z_][A-Za-z0-9_]*$
        """
        self._mapping = mapping

        for k, v in self._mapping.items():
            if not str.isidentifier(k) or keyword.iskeyword(k):
                raise ValueError(f"'{k}' is not an identifier name.")
            if not str.isidentifier(v) or keyword.iskeyword(v):
                raise ValueError(f"'{v}' is not an identifier name.")

    def _replace_args(self, args: list[ast.arg]) -> list[ast.arg]:
        """Helper function to replace arg names."""
        pass

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        """Visit a FunctionDef node."""
        pass

    def visit_Name(self, node: ast.Name) -> ast.Name:
        """Visit a Name node."""
        pass
