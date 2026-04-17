"""Codegen for single expressions."""
from __future__ import annotations
import ast
import re
from latexify import analyzers, ast_utils, exceptions
from latexify.codegen import codegen_utils, expression_rules, identifier_converter

class ExpressionCodegen(ast.NodeVisitor):
    """Codegen for single expressions."""
    _identifier_converter: identifier_converter.IdentifierConverter
    _bin_op_rules: dict[type[ast.operator], expression_rules.BinOpRule]
    _compare_ops: dict[type[ast.cmpop], str]

    def __init__(self, *, use_math_symbols: bool=False, use_set_symbols: bool=False, escape_underscores: bool=True) -> None:
        """Initializer.

        Args:
            use_math_symbols: Whether to convert identifiers with a math symbol
                surface (e.g., "alpha") to the LaTeX symbol (e.g., "\\alpha").
            use_set_symbols: Whether to use set symbols or not.
        """
        self._identifier_converter = identifier_converter.IdentifierConverter(use_math_symbols=use_math_symbols, escape_underscores=escape_underscores)
        self._bin_op_rules = expression_rules.SET_BIN_OP_RULES if use_set_symbols else expression_rules.BIN_OP_RULES
        self._compare_ops = expression_rules.SET_COMPARE_OPS if use_set_symbols else expression_rules.COMPARE_OPS

    def generic_visit(self, node: ast.AST) -> str:
        pass

    def visit_Tuple(self, node: ast.Tuple) -> str:
        """Visit a Tuple node."""
        pass

    def visit_List(self, node: ast.List) -> str:
        """Visit a List node."""
        pass

    def visit_Set(self, node: ast.Set) -> str:
        """Visit a Set node."""
        pass

    def visit_ListComp(self, node: ast.ListComp) -> str:
        """Visit a ListComp node."""
        pass

    def visit_SetComp(self, node: ast.SetComp) -> str:
        """Visit a SetComp node."""
        pass

    def visit_comprehension(self, node: ast.comprehension) -> str:
        """Visit a comprehension node."""
        pass

    def _generate_sum_prod(self, node: ast.Call) -> str | None:
        """Generates sum/prod expression.

        Args:
            node: ast.Call node containing the sum/prod invocation.

        Returns:
            Generated LaTeX, or None if the node has unsupported syntax.
        """
        pass

    def _generate_matrix(self, node: ast.Call) -> str | None:
        """Generates matrix expression.

        Args:
            node: ast.Call node containing the ndarray invocation.

        Returns:
            Generated LaTeX, or None if the node has unsupported syntax.
        """
        pass

    def _generate_zeros(self, node: ast.Call) -> str | None:
        """Generates LaTeX for numpy.zeros.
        Args:
            node: ast.Call node containing the appropriate method invocation.
        Returns:
            Generated LaTeX, or None if the node has unsupported syntax.
        """
        pass

    def _generate_identity(self, node: ast.Call) -> str | None:
        """Generates LaTeX for numpy.identity.
        Args:
            node: ast.Call node containing the appropriate method invocation.
        Returns:
            Generated LaTeX, or None if the node has unsupported syntax.
        """
        pass

    def _generate_transpose(self, node: ast.Call) -> str | None:
        """Generates LaTeX for numpy.transpose.
        Args:
            node: ast.Call node containing the appropriate method invocation.
        Returns:
            Generated LaTeX, or None if the node has unsupported syntax.
        Raises:
            LatexifyError: Unsupported argument type given.
        """
        pass

    def _generate_determinant(self, node: ast.Call) -> str | None:
        """Generates LaTeX for numpy.linalg.det.
        Args:
            node: ast.Call node containing the appropriate method invocation.
        Returns:
            Generated LaTeX, or None if the node has unsupported syntax.
        Raises:
            LatexifyError: Unsupported argument type given.
        """
        pass

    def _generate_matrix_rank(self, node: ast.Call) -> str | None:
        """Generates LaTeX for numpy.linalg.matrix_rank.
        Args:
            node: ast.Call node containing the appropriate method invocation.
        Returns:
            Generated LaTeX, or None if the node has unsupported syntax.
        Raises:
            LatexifyError: Unsupported argument type given.
        """
        pass

    def _generate_matrix_power(self, node: ast.Call) -> str | None:
        """Generates LaTeX for numpy.linalg.matrix_power.
        Args:
            node: ast.Call node containing the appropriate method invocation.
        Returns:
            Generated LaTeX, or None if the node has unsupported syntax.
        Raises:
            LatexifyError: Unsupported argument type given.
        """
        pass

    def _generate_inv(self, node: ast.Call) -> str | None:
        """Generates LaTeX for numpy.linalg.inv.
        Args:
            node: ast.Call node containing the appropriate method invocation.
        Returns:
            Generated LaTeX, or None if the node has unsupported syntax.
        Raises:
            LatexifyError: Unsupported argument type given.
        """
        pass

    def _generate_pinv(self, node: ast.Call) -> str | None:
        """Generates LaTeX for numpy.linalg.pinv.
        Args:
            node: ast.Call node containing the appropriate method invocation.
        Returns:
            Generated LaTeX, or None if the node has unsupported syntax.
        Raises:
            LatexifyError: Unsupported argument type given.
        """
        pass

    def visit_Call(self, node: ast.Call) -> str:
        """Visit a Call node."""
        pass

    def visit_Attribute(self, node: ast.Attribute) -> str:
        """Visit an Attribute node."""
        pass

    def visit_Name(self, node: ast.Name) -> str:
        """Visit a Name node."""
        pass

    def visit_Constant(self, node: ast.Constant) -> str:
        """Visit a Constant node."""
        pass

    def visit_Num(self, node: ast.Num) -> str:
        """Visit a Num node."""
        pass

    def visit_Str(self, node: ast.Str) -> str:
        """Visit a Str node."""
        pass

    def visit_Bytes(self, node: ast.Bytes) -> str:
        """Visit a Bytes node."""
        pass

    def visit_NameConstant(self, node: ast.NameConstant) -> str:
        """Visit a NameConstant node."""
        pass

    def visit_Ellipsis(self, node: ast.Ellipsis) -> str:
        """Visit an Ellipsis node."""
        pass

    def _wrap_operand(self, child: ast.expr, parent_prec: int, force_wrap: bool=False) -> str:
        """Wraps the operand subtree with parentheses.

        Args:
            child: Operand subtree.
            parent_prec: Precedence of the parent operator.
            force_wrap: Whether to wrap the operand or not when the precedence is equal.

        Returns:
            LaTeX form of `child`, with or without surrounding parentheses.
        """
        pass

    def _wrap_binop_operand(self, child: ast.expr, parent_prec: int, operand_rule: expression_rules.BinOperandRule) -> str:
        """Wraps the operand subtree of BinOp with parentheses.

        Args:
            child: Operand subtree.
            parent_prec: Precedence of the parent operator.
            operand_rule: Syntax rule of this operand.

        Returns:
            LaTeX form of the `child`, with or without surrounding parentheses.
        """
        pass
    _l_bracket_pattern = re.compile('^\\\\mathopen.*')
    _r_bracket_pattern = re.compile('.*\\\\mathclose[^ ]+$')
    _r_word_pattern = re.compile('\\\\mathrm\\{[^ ]+\\}$')

    def _should_remove_multiply_op(self, l_latex: str, r_latex: str, l_expr: ast.expr, r_expr: ast.expr):
        """Determine whether the multiply operator should be removed or not.

        See also:
        https://github.com/google/latexify_py/issues/89#issuecomment-1344967636

        This is an ad-hoc implementation.
        This function doesn't fully implements the above requirements, but only
        essential ones necessary to release v0.3.
        """
        pass

    def visit_BinOp(self, node: ast.BinOp) -> str:
        """Visit a BinOp node."""
        pass

    def visit_UnaryOp(self, node: ast.UnaryOp) -> str:
        """Visit a UnaryOp node."""
        pass

    def visit_Compare(self, node: ast.Compare) -> str:
        """Visit a Compare node."""
        pass

    def visit_BoolOp(self, node: ast.BoolOp) -> str:
        """Visit a BoolOp node."""
        pass

    def visit_IfExp(self, node: ast.IfExp) -> str:
        """Visit an IfExp node"""
        pass

    def _get_sum_prod_range(self, node: ast.comprehension) -> tuple[str, str] | None:
        """Helper to process range(...) for sum and prod functions.

        Args:
            node: comprehension node to be analyzed.

        Returns:
            Tuple of following strings:
                - lower_rhs
                - upper
            which are used in _get_sum_prod_info, or None if the analysis failed.
        """
        pass

    def _get_sum_prod_info(self, node: ast.GeneratorExp) -> tuple[str, list[tuple[str, str]]]:
        """Process GeneratorExp for sum and prod functions.

        Args:
            node: GeneratorExp node to be analyzed.

        Returns:
            Tuple of following strings:
                - elt
                - scripts
            which are used to represent sum/prod operators as follows:
                \\sum_{scripts[0][0]}^{scripts[0][1]}
                    \\sum_{scripts[1][0]}^{scripts[1][1]}
                    ...
                    {elt}

        Raises:
            LateixfyError: Unsupported AST is given.
        """
        pass

    def visit_Index(self, node: ast.Index) -> str:
        """Visit an Index node."""
        pass

    def _convert_nested_subscripts(self, node: ast.Subscript) -> tuple[str, list[str]]:
        """Helper function to convert nested subscription.

        This function converts x[i][j][...] to "x" and ["i", "j", ...]

        Args:
            node: ast.Subscript node to be converted.

        Returns:
            Tuple of following strings:
                - The root value of the subscription.
                - Sequence of incices.
        """
        pass

    def visit_Subscript(self, node: ast.Subscript) -> str:
        """Visitor a Subscript node."""
        pass
