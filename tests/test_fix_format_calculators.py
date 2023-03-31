from . import utils
from fix_format_demonstration import fix_format_readers
from fix_format_demonstration.operation_tree import OperationTree, OperationTreeNode, OperationTreeEvaluationError
import pytest


class TestPostfix:

    def test_addition(self):
        equation = "2 3 +"
        answer = 5.0

        assert fix_format_readers.calculate_postfix(equation) == answer
    
    def test_subtraction(self):
        equation = "2 3 -"
        answer = -1.0

        assert fix_format_readers.calculate_postfix(equation) == answer
    
    def test_multiplication(self):
        equation = "2 3 *"
        answer = 6.0

        assert fix_format_readers.calculate_postfix(equation) == answer
    
    def test_division(self):
        equation = "2 3 /"
        answer = 0.66
        err = 0.01

        assert utils.float_within_error(fix_format_readers.calculate_postfix(equation), answer, err)
    
    def test_dangling_operator_error(self):
        equation = "2 3 + +"
        with pytest.raises(fix_format_readers.InvalidPostfixExpressionError):
            fix_format_readers.calculate_postfix(equation)
    
    def test_extra_operand_at_end_error(self):
        equation = "2 3 + 4"
        with pytest.raises(fix_format_readers.InvalidPostfixExpressionError):
            fix_format_readers.calculate_postfix(equation)
    
    def test_extra_operand_at_beginning_error(self):
        equation = "2 3 4 +"
        with pytest.raises(fix_format_readers.InvalidPostfixExpressionError):
            fix_format_readers.calculate_postfix(equation)

    def test_multiple_operations(self):
        equation_answer_pairs = {
            "2 3 + 4 +" : 9.0,
            "2 3 4 + +" : 9.0,
            "4 2 * 2 /" : 4.0,
            "4 2 2 * /" : 1.0,
            "3 4 * 2 7 / +" : 12.285,
        }
        err = 0.001

        for equation, answer in zip(equation_answer_pairs.keys(), equation_answer_pairs.values()):
            assert utils.float_within_error(fix_format_readers.calculate_postfix(equation), answer, err)


class TestPrefix:

    def test_addition(self):
        equation = "+ 2 3"
        answer = 5.0

        assert fix_format_readers.calculate_prefix(equation) == answer
    
    def test_subtraction(self):
        equation = "- 2 3"
        answer = -1.0

        assert fix_format_readers.calculate_prefix(equation) == answer
    
    def test_multiplication(self):
        equation = "* 2 3"
        answer = 6.0

        assert fix_format_readers.calculate_prefix(equation) == answer
    
    def test_division(self):
        equation = "/ 2 3"
        answer = 0.66
        err = 0.01

        assert utils.float_within_error(fix_format_readers.calculate_prefix(equation), answer, err)
    
    def test_empty_error(self):
        equation = "2 3 + +"
        with pytest.raises(fix_format_readers.InvalidPrefixExpressionError):
            fix_format_readers.calculate_prefix(equation)

    def test_multiple_operations(self):
        equation_answer_pairs = {
            "+ + 2 3 4" : 9.0,
            "+ 2 + 3 4" : 9.0,
            "/ * 4 2 2" : 4.0,
            "/ 4 * 2 2" : 1.0,
            "+ * 3 4 / 2 7" : 12.285,
            "- * / 1 2 + 3 4 + * 5 6 / 7 8" : -27.375
        }
        err = 0.001

        for equation, answer in zip(equation_answer_pairs.keys(), equation_answer_pairs.values()):
            assert utils.float_within_error(fix_format_readers.calculate_prefix(equation), answer, err)


class TestInfix:

    def test_addition(self):
        equation = "2 + 3"
        answer = 5.0

        assert fix_format_readers.calculate_infix(equation) == answer
    
    def test_subtraction(self):
        equation = "2 - 3"
        answer = -1.0

        assert fix_format_readers.calculate_infix(equation) == answer
    
    def test_multiplication(self):
        equation = "2 * 3"
        answer = 6.0

        assert fix_format_readers.calculate_infix(equation) == answer
    
    def test_division(self):
        equation = "2 / 3"
        answer = 0.66
        err = 0.01

        assert utils.float_within_error(fix_format_readers.calculate_infix(equation), answer, err)
    
    def test_dangling_operator_error(self):
        equation = "2 + 3 +"
        with pytest.raises(fix_format_readers.InvalidInfixExpressionError):
            fix_format_readers.calculate_infix(equation)
    
    def test_misplaced_operator_error(self):
        equation = "1 2 + 3 +"
        with pytest.raises(fix_format_readers.InvalidInfixExpressionError):
            fix_format_readers.calculate_infix(equation)
    
    def test_missing_operand_error(self):
        equation = "2 + + 3"
        with pytest.raises(fix_format_readers.InvalidInfixExpressionError):
            fix_format_readers.calculate_infix(equation)
    
    def test_misplaced_operand_error(self):
        equation = "1 2 + + 3"
        with pytest.raises(fix_format_readers.InvalidInfixExpressionError):
            fix_format_readers.calculate_infix(equation)
    
    def test_missing_close_paren_error(self):
        equation = "2 + ( 3 + 4"
        with pytest.raises(fix_format_readers.InvalidInfixExpressionError):
            fix_format_readers.calculate_infix(equation)
    
    def test_missing_operator_error(self):
        equation = "2 ( 3 + 4 )"
        with pytest.raises(fix_format_readers.InvalidInfixExpressionError):
            fix_format_readers.calculate_infix(equation)
    
    def test_operator_before_closed_paren_error(self):
        equation = "2 ( 3 + 4 + )"
        with pytest.raises(fix_format_readers.InvalidInfixExpressionError):
            fix_format_readers.calculate_infix(equation)
    
    def test_missing_open_paren_error(self):
        equation = "2 + 3 + 4 )"
        with pytest.raises(fix_format_readers.InvalidInfixExpressionError):
            fix_format_readers.calculate_infix(equation)

    def test_multiple_operations(self):
        equation_answer_pairs = {
            "2 + ( 3 + 4 )" : 9.0,
            "( 2 + 3 ) + 4" : 9.0,
            "4 * 2 / 2" : 4.0,
            "4 / 2 * 2" : 4.0,
            "4 / ( 2 * 2 )" : 1.0,
            "3 * 4 + 2 / 7" : 12.285,
            "3 * ( 4 + 2 ) / 7" : 2.571,
            "( ( 1 / 2 ) * ( 3 + 4 ) ) - ( ( 5 * 6 ) + ( 7 / 8 ) )" : -27.375,
            "( 1 / 2 * ( 3 + 4 ) ) - ( 5 * 6 + 7 / 8 )" : -27.375
        }
        err = 0.001

        for equation, answer in zip(equation_answer_pairs.keys(), equation_answer_pairs.values()):
            assert utils.float_within_error(fix_format_readers.calculate_infix(equation), answer, err)
