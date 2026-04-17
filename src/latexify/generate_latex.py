"""Generate LaTeX code."""

from __future__ import annotations

import enum
from collections.abc import Callable
from typing import Any

from latexify import codegen
from latexify import config as cfg
from latexify import parser, transformers


class Style(enum.Enum):
    """The style of the generated LaTeX."""

    ALGORITHMIC = "algorithmic"
    FUNCTION = "function"
    IPYTHON_ALGORITHMIC = "ipython-algorithmic"


def get_latex(
    fn: Callable[..., Any],
    *,
    style: Style = Style.FUNCTION,
    config: cfg.Config | None = None,
    **kwargs,
) -> str:
    """Obtains LaTeX description from the function's source.

    Args:
        fn: Reference to a function to analyze.
        style: Style of the LaTeX description, the default is FUNCTION.
        config: Use defined Config object, if it is None, it will be automatic assigned
            with default value.
        **kwargs: Dict of Config field values that could be defined individually
            by users.

    Returns:
        Generated LaTeX description.

    Raises:
        latexify.exceptions.LatexifyError: Something went wrong during conversion.
    """
    pass
