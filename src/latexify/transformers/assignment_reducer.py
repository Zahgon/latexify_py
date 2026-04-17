"""NodeTransformer to reduce assigned expressions."""

from __future__ import annotations

import ast
from typing import Any

from latexify import ast_utils, exceptions


class AssignmentReducer(ast.NodeTransformer):
    """NodeTransformer to reduce assigned expressions.

    This class replaces a functions with multiple assignments to a function with only
    single return.

    Example:
        def f(x):
            y = 2 + x
            z = 3 * y
            return 4 + z

        AssignmentReducer modifies the function above to below:

        def f(x):
            return 4 + 3 * (2 + x)
    """

    _assignments: dict[str, ast.expr] | None = None

    # TODO(odashi):
    # Currently, this function does not care much about some expressions, e.g.,
    # comprehensions or lambdas, which introduces inner scopes.
    # It may cause some mistakes in the resulting AST.
    def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
        """Visit a FunctionDef node."""
        pass

    def visit_Name(self, node: ast.Name) -> Any:
        """Visit a Name node."""
        pass
