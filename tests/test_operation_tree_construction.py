from . import utils
from fix_format_demonstration import fix_format_readers
from fix_format_demonstration.operation_tree import OperationTree, OperationTreeNode, OperationTreeEvaluationError
import pytest


class TestOperationTreeFromPostFix:

    def test_addition(self):
        equation = "2 3 +"
        answer = 5.0
        err = 0.01

        tree = fix_format_readers.postfix_to_operation_tree(equation)
        
        solver_solution = fix_format_readers.calculate_postfix(equation)
        tree_solution = tree.evaluate_tree()

        assert utils.float_within_error(solver_solution, tree_solution, err) == True
        assert utils.float_within_error(tree_solution, answer, err) == True
    
    def test_subtraction(self):
        equation = "2 3 -"
        answer = -1.0
        err = 0.01

        tree = fix_format_readers.postfix_to_operation_tree(equation)
        
        solver_solution = fix_format_readers.calculate_postfix(equation)
        tree_solution = tree.evaluate_tree()

        assert utils.float_within_error(solver_solution, tree_solution, err) == True
        assert utils.float_within_error(tree_solution, answer, err) == True
    
    def test_multiplication(self):
        equation = "2 3 *"
        answer = 6.0
        err = 0.01

        tree = fix_format_readers.postfix_to_operation_tree(equation)
        
        solver_solution = fix_format_readers.calculate_postfix(equation)
        tree_solution = tree.evaluate_tree()

        assert utils.float_within_error(solver_solution, tree_solution, err) == True
        assert utils.float_within_error(tree_solution, answer, err) == True
    
    def test_division(self):
        equation = "2 3 /"
        answer = 0.66
        err = 0.01

        tree = fix_format_readers.postfix_to_operation_tree(equation)
        
        solver_solution = fix_format_readers.calculate_postfix(equation)
        tree_solution = tree.evaluate_tree()

        assert utils.float_within_error(solver_solution, tree_solution, err) == True
        assert utils.float_within_error(tree_solution, answer, err) == True
    
    def test_dangling_operator_error(self):
        equation = "2 3 + +"
        with pytest.raises(fix_format_readers.InvalidPostfixExpressionError):
            tree = fix_format_readers.postfix_to_operation_tree(equation)
    
    def test_extra_operand_at_end_error(self):
        equation = "2 3 + 4"
        with pytest.raises(fix_format_readers.InvalidPostfixExpressionError):
            tree = fix_format_readers.postfix_to_operation_tree(equation)
    
    def test_extra_operand_at_begining_error(self):
        equation = "2 3 4 +"
        with pytest.raises(fix_format_readers.InvalidPostfixExpressionError):
            tree = fix_format_readers.postfix_to_operation_tree(equation)

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
            tree = fix_format_readers.postfix_to_operation_tree(equation)

            solver_solution = fix_format_readers.calculate_postfix(equation)
            tree_solution = tree.evaluate_tree()

            assert utils.float_within_error(solver_solution, tree_solution, err) == True
            assert utils.float_within_error(tree_solution, answer, err) == True


class TestOperationTreeFromPrefix:

    def test_addition(self):
        equation = "+ 2 3"
        answer = 5.0
        err = 0.01

        tree = fix_format_readers.prefix_to_operation_tree(equation)
        
        solver_solution = fix_format_readers.calculate_prefix(equation)
        tree_solution = tree.evaluate_tree()

        assert utils.float_within_error(solver_solution, tree_solution, err) == True
        assert utils.float_within_error(tree_solution, answer, err) == True
    
    def test_subtraction(self):
        equation = "- 2 3"
        answer = -1.0
        err = 0.01

        tree = fix_format_readers.prefix_to_operation_tree(equation)
        
        solver_solution = fix_format_readers.calculate_prefix(equation)
        tree_solution = tree.evaluate_tree()

        assert utils.float_within_error(solver_solution, tree_solution, err) == True
        assert utils.float_within_error(tree_solution, answer, err) == True
    
    def test_multiplication(self):
        equation = "* 2 3"
        answer = 6.0
        err = 0.01

        tree = fix_format_readers.prefix_to_operation_tree(equation)
        
        solver_solution = fix_format_readers.calculate_prefix(equation)
        tree_solution = tree.evaluate_tree()

        assert utils.float_within_error(solver_solution, tree_solution, err) == True
        assert utils.float_within_error(tree_solution, answer, err) == True
    
    def test_division(self):
        equation = "/ 2 3"
        answer = 0.66
        err = 0.01

        tree = fix_format_readers.prefix_to_operation_tree(equation)
        
        solver_solution = fix_format_readers.calculate_prefix(equation)
        tree_solution = tree.evaluate_tree()

        assert utils.float_within_error(solver_solution, tree_solution, err) == True
        assert utils.float_within_error(tree_solution, answer, err) == True
    
    def test_empty_error(self):
        equation = "2 3 + +"
        with pytest.raises(fix_format_readers.InvalidPrefixExpressionError):
            tree = fix_format_readers.prefix_to_operation_tree(equation)

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
            tree = fix_format_readers.prefix_to_operation_tree(equation)
            
            solver_solution = fix_format_readers.calculate_prefix(equation)
            tree_solution = tree.evaluate_tree()

            assert utils.float_within_error(solver_solution, tree_solution, err) == True
            assert utils.float_within_error(tree_solution, answer, err) == True


class TestInfix:

    def test_addition(self):
        equation = "2 + 3"
        answer = 5.0
        err = 0.01

        tree = fix_format_readers.infix_to_operation_tree(equation)
        
        solver_solution = fix_format_readers.calculate_infix(equation)
        tree_solution = tree.evaluate_tree()

        assert utils.float_within_error(solver_solution, tree_solution, err) == True
        assert utils.float_within_error(tree_solution, answer, err) == True
    
    def test_subtraction(self):
        equation = "2 - 3"
        answer = -1.0
        err = 0.01

        tree = fix_format_readers.infix_to_operation_tree(equation)
        
        solver_solution = fix_format_readers.calculate_infix(equation)
        tree_solution = tree.evaluate_tree()

        assert utils.float_within_error(solver_solution, tree_solution, err) == True
        assert utils.float_within_error(tree_solution, answer, err) == True
    
    def test_multiplication(self):
        equation = "2 * 3"
        answer = 6.0
        err = 0.01

        tree = fix_format_readers.infix_to_operation_tree(equation)
        
        solver_solution = fix_format_readers.calculate_infix(equation)
        tree_solution = tree.evaluate_tree()

        assert utils.float_within_error(solver_solution, tree_solution, err) == True
        assert utils.float_within_error(tree_solution, answer, err) == True
    
    def test_division(self):
        equation = "2 / 3"
        answer = 0.66
        err = 0.01

        tree = fix_format_readers.infix_to_operation_tree(equation)
        
        solver_solution = fix_format_readers.calculate_infix(equation)
        tree_solution = tree.evaluate_tree()

        assert utils.float_within_error(solver_solution, tree_solution, err) == True
        assert utils.float_within_error(tree_solution, answer, err) == True
    
    def test_dangling_operator_error(self):
        equation = "2 + 3 +"
        with pytest.raises(fix_format_readers.InvalidInfixExpressionError):
            fix_format_readers.infix_to_operation_tree(equation)
    
    def test_misplaced_operator_error(self):
        equation = "1 2 + 3 +"
        with pytest.raises(fix_format_readers.InvalidInfixExpressionError):
            fix_format_readers.infix_to_operation_tree(equation)
    
    def test_missing_operand_error(self):
        equation = "2 + + 3"
        with pytest.raises(fix_format_readers.InvalidInfixExpressionError):
            fix_format_readers.infix_to_operation_tree(equation)
    
    def test_misplaced_operand_error(self):
        equation = "1 2 + + 3"
        with pytest.raises(fix_format_readers.InvalidInfixExpressionError):
            fix_format_readers.infix_to_operation_tree(equation)
    
    def test_missing_close_paran_error(self):
        equation = "2 + ( 3 + 4"
        with pytest.raises(fix_format_readers.InvalidInfixExpressionError):
            fix_format_readers.infix_to_operation_tree(equation)
    
    def test_missing_operator_error(self):
        equation = "2 ( 3 + 4 )"
        with pytest.raises(fix_format_readers.InvalidInfixExpressionError):
            fix_format_readers.infix_to_operation_tree(equation)
    
    def test_operator_before_closed_paran_error(self):
        equation = "2 ( 3 + 4 + )"
        with pytest.raises(fix_format_readers.InvalidInfixExpressionError):
            fix_format_readers.infix_to_operation_tree(equation)
    
    def test_missing_open_paran_error(self):
        equation = "2 + 3 + 4 )"
        with pytest.raises(fix_format_readers.InvalidInfixExpressionError):
            fix_format_readers.infix_to_operation_tree(equation)

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
            tree = fix_format_readers.infix_to_operation_tree(equation)
            
            solver_solution = fix_format_readers.calculate_infix(equation)
            tree_solution = tree.evaluate_tree()

            assert utils.float_within_error(solver_solution, tree_solution, err) == True
            assert utils.float_within_error(tree_solution, answer, err) == True
