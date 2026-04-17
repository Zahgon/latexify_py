"""Parsing utilities."""

from __future__ import annotations

import ast
import inspect
import textwrap
from collections.abc import Callable
from typing import Any

import dill  # type: ignore[import]

from latexify import exceptions


def parse_function(fn: Callable[..., Any]) -> ast.Module:
    """Parses given function.

    Args:
        fn: Target function.

    Returns:
        AST tree representing `fn`.
    """
    pass
