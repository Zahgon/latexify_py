"""Frontend interfaces of latexify."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, overload

from latexify import ipython_wrappers


@overload
def algorithmic(
    fn: Callable[..., Any], **kwargs: Any
) -> ipython_wrappers.LatexifiedAlgorithm: ...


@overload
def algorithmic(
    **kwargs: Any,
) -> Callable[[Callable[..., Any]], ipython_wrappers.LatexifiedAlgorithm]: ...


def algorithmic(
    fn: Callable[..., Any] | None = None, **kwargs: Any
) -> (
    ipython_wrappers.LatexifiedAlgorithm
    | Callable[[Callable[..., Any]], ipython_wrappers.LatexifiedAlgorithm]
):
    """Attach LaTeX pretty-printing to the given function.

    This function works with or without specifying the target function as the
    positional argument. The following two syntaxes works similarly.
        - latexify.algorithmic(alg, **kwargs)
        - latexify.algorithmic(**kwargs)(alg)

    Args:
        fn: Callable to be wrapped.
        **kwargs: Arguments to control behavior. See also get_latex().

    Returns:
        - If `fn` is passed, returns the wrapped function.
        - Otherwise, returns the wrapper function with given settings.
    """
    pass


@overload
def function(
    fn: Callable[..., Any], **kwargs: Any
) -> ipython_wrappers.LatexifiedFunction: ...


@overload
def function(
    **kwargs: Any,
) -> Callable[[Callable[..., Any]], ipython_wrappers.LatexifiedFunction]: ...


def function(
    fn: Callable[..., Any] | None = None, **kwargs: Any
) -> (
    ipython_wrappers.LatexifiedFunction
    | Callable[[Callable[..., Any]], ipython_wrappers.LatexifiedFunction]
):
    """Attach LaTeX pretty-printing to the given function.

    This function works with or without specifying the target function as the positional
    argument. The following two syntaxes works similarly.
        - latexify.function(fn, **kwargs)
        - latexify.function(**kwargs)(fn)

    Args:
        fn: Callable to be wrapped.
        **kwargs: Arguments to control behavior. See also get_latex().

    Returns:
        - If `fn` is passed, returns the wrapped function.
        - Otherwise, returns the wrapper function with given settings.
    """
    pass


@overload
def expression(
    fn: Callable[..., Any], **kwargs: Any
) -> ipython_wrappers.LatexifiedFunction: ...


@overload
def expression(
    **kwargs: Any,
) -> Callable[[Callable[..., Any]], ipython_wrappers.LatexifiedFunction]: ...


def expression(
    fn: Callable[..., Any] | None = None, **kwargs: Any
) -> (
    ipython_wrappers.LatexifiedFunction
    | Callable[[Callable[..., Any]], ipython_wrappers.LatexifiedFunction]
):
    """Attach LaTeX pretty-printing to the given function.

    This function is a shortcut for `latexify.function` with the default parameter
    `use_signature=False`.
    """
    pass
