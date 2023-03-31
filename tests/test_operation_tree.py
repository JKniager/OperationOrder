from . import utils
from fix_format_demonstration.operation_tree import OperationTree, OperationTreeNode
import pytest


class TestOperationTreeIsValidRecursiveTrue:

    def test_single_number(self):
        root = OperationTreeNode("4", None)
        tree = OperationTree(root)

        assert tree.is_tree_valid_recursive() == True
    
    def test_operator_with_args(self):
        root = OperationTreeNode("+", None)
        root.setLeft(OperationTreeNode("4", None))
        root.setRight(OperationTreeNode("2", None))
        tree = OperationTree(root)

        assert tree.is_tree_valid_recursive() == True
    
    def test_multiple_operators(self):
        root = OperationTreeNode("+", None)
        multi = OperationTreeNode("*", None)
        multi.setLeft(OperationTreeNode("3", None))
        multi.setRight(OperationTreeNode("4", None))
        divis = OperationTreeNode("/", None)
        divis.setLeft(OperationTreeNode("2", None))
        divis.setRight(OperationTreeNode("7", None))

        root.setLeft(multi)
        root.setRight(divis)

        tree = OperationTree(root)

        assert tree.is_tree_valid_recursive() == True
    
    def test_unbalanced_left_tree(self):
        root = OperationTreeNode("+", None)
        second_add = OperationTreeNode("+", None)
        second_add.setLeft(OperationTreeNode("2", None))
        second_add.setRight(OperationTreeNode("3", None))
        root.setLeft(second_add)
        root.setRight(OperationTreeNode("4", None))

        tree = OperationTree(root)

        assert tree.is_tree_valid_recursive() == True
    
    def test_unbalanced_right_tree(self):
        "+ 2 + 3 4"
        root = OperationTreeNode("+", None)
        second_add = OperationTreeNode("+", None)
        second_add.setLeft(OperationTreeNode("3", None))
        second_add.setRight(OperationTreeNode("4", None))
        root.setLeft(OperationTreeNode("2", None))
        root.setRight(second_add)

        tree = OperationTree(root)

        assert tree.is_tree_valid_recursive() == True


class TestOperationTreeIsValidRecursiveFalse:

    def test_single_operator(self):
        root = OperationTreeNode("+", None)
        tree = OperationTree(root)

        assert tree.is_tree_valid_recursive() == False
    
    def test_operator_with_missing_args(self):
        root = OperationTreeNode("+", None)
        root.setLeft(OperationTreeNode("4", None))
        tree = OperationTree(root)

        assert tree.is_tree_valid_recursive() == False
    
    def test_multiple_operators(self):
        root = OperationTreeNode("+", None)
        multi = OperationTreeNode("*", None)
        multi.setLeft(OperationTreeNode("3", None))
        multi.setRight(OperationTreeNode("4", None))
        divis = OperationTreeNode("/", None)
        divis.setLeft(OperationTreeNode("2", None))

        root.setLeft(multi)
        root.setRight(divis)

        tree = OperationTree(root)

        assert tree.is_tree_valid_recursive() == False
    
    def test_constant_with_operator_child(self):
        root = OperationTreeNode("4", None)
        root.setLeft(OperationTreeNode("+", None))
        tree = OperationTree(root)

        assert tree.is_tree_valid_recursive() == False


class TestOperationTreeEvaluateTreeRecursive:

    def test_single_constant(self):
        root = OperationTreeNode("4", None)
        tree = OperationTree(root)

        assert tree.evaluate_tree_recursive() == 4
    
    def test_operator_with_args(self):
        root = OperationTreeNode("+", None)
        root.setLeft(OperationTreeNode("4", None))
        root.setRight(OperationTreeNode("2", None))
        tree = OperationTree(root)

        assert tree.evaluate_tree_recursive() == 6
    
    def test_multiple_operators(self):
        root = OperationTreeNode("+", None)
        multi = OperationTreeNode("*", None)
        multi.setLeft(OperationTreeNode("3", None))
        multi.setRight(OperationTreeNode("4", None))
        divis = OperationTreeNode("/", None)
        divis.setLeft(OperationTreeNode("2", None))
        divis.setRight(OperationTreeNode("7", None))

        root.setLeft(multi)
        root.setRight(divis)

        tree = OperationTree(root)

        assert utils.float_within_error(tree.evaluate_tree_recursive(), 12.2857, 0.0001) == True
    
    def test_big_tree(self):
        # [(1 / 2) * (3 + 4)] - [(5 * 6) + (7 / 8)]
        root = OperationTreeNode('-', None)

        root.setLeft(OperationTreeNode('*', None))
        root._left_child.setLeft(OperationTreeNode('/', None))
        root._left_child._left_child.setLeft(OperationTreeNode('1', None))
        root._left_child._left_child.setRight(OperationTreeNode('2', None))
        root._left_child.setRight(OperationTreeNode('+', None))
        root._left_child._right_child.setLeft(OperationTreeNode('3', None))
        root._left_child._right_child.setRight(OperationTreeNode('4', None))

        root.setRight(OperationTreeNode('+', None))
        root._right_child.setLeft(OperationTreeNode('*', None))
        root._right_child._left_child.setLeft(OperationTreeNode('5', None))
        root._right_child._left_child.setRight(OperationTreeNode('6', None))
        root._right_child.setRight(OperationTreeNode('/', None))
        root._right_child._right_child.setLeft(OperationTreeNode('7', None))
        root._right_child._right_child.setRight(OperationTreeNode('8', None))

        tree = OperationTree(root)

        assert utils.float_within_error(tree.evaluate_tree_recursive(), -27.375, 0.001) == True


class TestOperationTreeIsValidTrue:

    def test_single_number(self):
        root = OperationTreeNode("4", None)
        tree = OperationTree(root)

        assert tree.is_tree_valid() == True
    
    def test_operator_with_args(self):
        root = OperationTreeNode("+", None)
        root.setLeft(OperationTreeNode("4", None))
        root.setRight(OperationTreeNode("2", None))
        tree = OperationTree(root)

        assert tree.is_tree_valid() == True
    
    def test_multiple_operators(self):
        root = OperationTreeNode("+", None)
        multi = OperationTreeNode("*", None)
        multi.setLeft(OperationTreeNode("3", None))
        multi.setRight(OperationTreeNode("4", None))
        divis = OperationTreeNode("/", None)
        divis.setLeft(OperationTreeNode("2", None))
        divis.setRight(OperationTreeNode("7", None))

        root.setLeft(multi)
        root.setRight(divis)

        tree = OperationTree(root)

        assert tree.is_tree_valid() == True
    
    def test_unbalanced_left_tree(self):
        root = OperationTreeNode("+", None)
        second_add = OperationTreeNode("+", None)
        second_add.setLeft(OperationTreeNode("2", None))
        second_add.setRight(OperationTreeNode("3", None))
        root.setLeft(second_add)
        root.setRight(OperationTreeNode("4", None))

        tree = OperationTree(root)

        assert tree.is_tree_valid() == True
    
    def test_unbalanced_right_tree(self):
        "+ 2 + 3 4"
        root = OperationTreeNode("+", None)
        second_add = OperationTreeNode("+", None)
        second_add.setLeft(OperationTreeNode("3", None))
        second_add.setRight(OperationTreeNode("4", None))
        root.setLeft(OperationTreeNode("2", None))
        root.setRight(second_add)

        tree = OperationTree(root)

        assert tree.is_tree_valid() == True


class TestOperationTreeIsValidFalse:

    def test_single_operator(self):
        root = OperationTreeNode("+", None)
        tree = OperationTree(root)

        assert tree.is_tree_valid() == False
    
    def test_operator_with_missing_args(self):
        root = OperationTreeNode("+", None)
        root.setLeft(OperationTreeNode("4", None))
        tree = OperationTree(root)

        assert tree.is_tree_valid() == False
    
    def test_multiple_operators(self):
        root = OperationTreeNode("+", None)
        multi = OperationTreeNode("*", None)
        multi.setLeft(OperationTreeNode("3", None))
        multi.setRight(OperationTreeNode("4", None))
        divis = OperationTreeNode("/", None)
        divis.setLeft(OperationTreeNode("2", None))

        root.setLeft(multi)
        root.setRight(divis)

        tree = OperationTree(root)

        assert tree.is_tree_valid() == False
    
    def test_constant_with_operator_child(self):
        root = OperationTreeNode("4", None)
        root.setLeft(OperationTreeNode("+", None))
        tree = OperationTree(root)

        assert tree.is_tree_valid() == False


class TestOperationTreeEvaluateTree:

    def test_single_constant(self):
        root = OperationTreeNode("4", None)
        tree = OperationTree(root)

        assert tree.evaluate_tree() == 4
    
    def test_operator_with_args(self):
        root = OperationTreeNode("+", None)
        root.setLeft(OperationTreeNode("4", None))
        root.setRight(OperationTreeNode("2", None))
        tree = OperationTree(root)

        assert tree.evaluate_tree() == 6
    
    def test_multiple_operators(self):
        root = OperationTreeNode("+", None)
        multi = OperationTreeNode("*", None)
        multi.setLeft(OperationTreeNode("3", None))
        multi.setRight(OperationTreeNode("4", None))
        divis = OperationTreeNode("/", None)
        divis.setLeft(OperationTreeNode("2", None))
        divis.setRight(OperationTreeNode("7", None))

        root.setLeft(multi)
        root.setRight(divis)

        tree = OperationTree(root)

        assert utils.float_within_error(tree.evaluate_tree(), 12.2857, 0.0001) == True
    
    def test_big_tree(self):
        # [(1 / 2) * (3 + 4)] - [(5 * 6) + (7 / 8)]
        root = OperationTreeNode('-', None)

        root.setLeft(OperationTreeNode('*', None))
        root._left_child.setLeft(OperationTreeNode('/', None))
        root._left_child._left_child.setLeft(OperationTreeNode('1', None))
        root._left_child._left_child.setRight(OperationTreeNode('2', None))
        root._left_child.setRight(OperationTreeNode('+', None))
        root._left_child._right_child.setLeft(OperationTreeNode('3', None))
        root._left_child._right_child.setRight(OperationTreeNode('4', None))

        root.setRight(OperationTreeNode('+', None))
        root._right_child.setLeft(OperationTreeNode('*', None))
        root._right_child._left_child.setLeft(OperationTreeNode('5', None))
        root._right_child._left_child.setRight(OperationTreeNode('6', None))
        root._right_child.setRight(OperationTreeNode('/', None))
        root._right_child._right_child.setLeft(OperationTreeNode('7', None))
        root._right_child._right_child.setRight(OperationTreeNode('8', None))

        tree = OperationTree(root)

        assert utils.float_within_error(tree.evaluate_tree(), -27.375, 0.001) == True
