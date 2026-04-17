"""Utilities to generate AST nodes."""

from __future__ import annotations

import ast
import sys
from typing import Any


def parse_expr(code: str) -> ast.expr:
    """Parses given Python expression.

    Args:
        code: Python expression to parse.

    Returns:
        ast.expr corresponding to `code`.
    """
    pass


def make_name(id: str) -> ast.Name:
    """Generates a new Name node.

    Args:
        id: Name of the node.

    Returns:
        Generated ast.Name.
    """
    return ast.Name(id=id, ctx=ast.Load())


def make_attribute(value: ast.expr, attr: str):
    """Generates a new Attribute node.

    Args:
        value: Parent value.
        attr: Attribute name.

    Returns:
        Generated ast.Attribute.
    """
    pass


def make_constant(value: Any) -> ast.expr:
    """Generates a new Constant node.

    Args:
        value: Value of the node.

    Returns:
        Generated ast.Constant or its equivalent.

    Raises:
        ValueError: Unsupported value type.
    """
    pass


def is_constant(node: ast.AST) -> bool:
    """Checks if the node is a constant.

    Args:
        node: The node to examine.

    Returns:
        True if the node is a constant, False otherwise.
    """
    pass


def is_str(node: ast.AST) -> bool:
    """Checks if the node is a str constant.

    Args:
        node: The node to examine.

    Returns:
        True if the node is a str constant, False otherwise.
    """
    pass


def extract_int_or_none(node: ast.expr) -> int | None:
    """Extracts int constant from the given Constant node.

    Args:
        node: ast.Constant or its equivalent representing an int value.

    Returns:
        Extracted int value, or None if extraction failed.
    """
    pass


def extract_int(node: ast.expr) -> int:
    """Extracts int constant from the given Constant node.

    Args:
        node: ast.Constant or its equivalent representing an int value.

    Returns:
        Extracted int value.

    Raises:
        ValueError: Not a subtree containing an int value.
    """
    pass


def extract_function_name_or_none(node: ast.Call) -> str | None:
    """Extracts function name from the given Call node.

    Args:
        node: ast.Call.

    Returns:
        Extracted function name, or None if not found.
    """
    pass


def create_function_def(
    name,
    args,
    body,
    decorator_list,
    returns=None,
    type_comment=None,
    type_params=None,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
) -> ast.FunctionDef:
    """Creates a FunctionDef node.

    This function generates an `ast.FunctionDef` node, optionally removing
    the `type_params` keyword argument for Python versions below 3.12.

    Args:
        name: Name of the function.
        args: Arguments of the function.
        body: Body of the function.
        decorator_list: List of decorators.
        returns: Return type of the function.
        type_comment: Type comment of the function.
        type_params: Type parameters of the function.
        lineno: Line number of the function definition.
        col_offset: Column offset of the function definition.
        end_lineno: End line number of the function definition.
        end_col_offset: End column offset of the function definition.

    Returns:
        ast.FunctionDef: The generated FunctionDef node.
    """
    pass
