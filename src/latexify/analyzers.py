"""Analyzer functions for specific subtrees."""

from __future__ import annotations

import ast
import dataclasses
import sys

from latexify import ast_utils, exceptions


@dataclasses.dataclass(frozen=True, eq=False)
class RangeInfo:
    """Information of the range function."""

    # Argument subtrees. These arguments could be shallow copies of the original
    # subtree.
    start: ast.expr
    stop: ast.expr
    step: ast.expr

    # Integer representation of each argument, when it is possible.
    start_int: int | None
    stop_int: int | None
    step_int: int | None


def analyze_range(node: ast.Call) -> RangeInfo:
    """Obtains RangeInfo from a Call subtree.

    Args:
        node: Subtree to be analyzed.

    Returns:
        RangeInfo extracted from `node`.

    Raises:
        LatexifySyntaxError: Analysis failed.
    """
    pass


def reduce_stop_parameter(node: ast.expr) -> ast.expr:
    """Adjusts the stop expression of the range.

    This function tries to convert the syntax as follows:
        * n + 1 --> n
        * n + 2 --> n + 1
        * n - 1 --> n - 2

    Args:
        node: The target expression.

    Returns:
        Converted expression.
    """
    pass
