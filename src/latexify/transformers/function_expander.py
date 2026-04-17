from __future__ import annotations

import ast
import functools
from collections.abc import Callable

from latexify import ast_utils, exceptions


# TODO(ZibingZhang): handle mutually recursive function expansions
class FunctionExpander(ast.NodeTransformer):
    """NodeTransformer to expand functions.

    This class replaces function calls with an expanded form.

    Example:
        def f(x, y):
            return hypot(x, y)

        FunctionExpander({"hypot"}) will modify the AST of the function above to below:

        def f(x, y):
            return sqrt(x**2, y**2)
    """

    def __init__(self, functions: set[str]) -> None:
        self._functions = functions

    def visit_Call(self, node: ast.Call) -> ast.AST:
        """Visit a Call node."""
        pass


def _atan2_expander(function_expander: FunctionExpander, node: ast.Call) -> ast.AST:
    pass


def _exp_expander(function_expander: FunctionExpander, node: ast.Call) -> ast.AST:
    pass


def _exp2_expander(function_expander: FunctionExpander, node: ast.Call) -> ast.AST:
    pass


def _expm1_expander(function_expander: FunctionExpander, node: ast.Call) -> ast.AST:
    pass


def _hypot_expander(function_expander: FunctionExpander, node: ast.Call) -> ast.AST:
    pass


def _log1p_expander(function_expander: FunctionExpander, node: ast.Call) -> ast.AST:
    pass


def _pow_expander(function_expander: FunctionExpander, node: ast.Call) -> ast.AST:
    pass


def _check_num_args(node: ast.Call, nargs: int) -> None:
    pass


_FUNCTION_EXPANDERS: dict[str, Callable[[FunctionExpander, ast.Call], ast.AST]] = {
    "atan2": _atan2_expander,
    "exp": _exp_expander,
    "exp2": _exp2_expander,
    "expm1": _expm1_expander,
    "hypot": _hypot_expander,
    "log1p": _log1p_expander,
    "pow": _pow_expander,
}
