from .utils import OperationEvaluator
from queue import LifoQueue


class OperationTreeNode:
    
    def __init__(self, value: str, parent: "OperationTreeNode") -> None:
        self._value = value
        self._parent = parent
        self._left_child = None
        self._right_child = None
    
    def setLeft(self, child: "OperationTreeNode") -> None:
        self._left_child = child
        self._left_child._parent = self
    
    def setRight(self, child: "OperationTreeNode") -> None:
        self._right_child = child
        self._right_child._parent = self


class OperationTreeEvaluationError(Exception):
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class OperationTree:

    def __init__(self, root: OperationTreeNode) -> None:
        self._root = root
    
    def is_tree_valid(self) -> bool:
        test_queue = LifoQueue()
        test_queue.put_nowait(self._root)

        while not test_queue.empty():
            cur_node: OperationTreeNode = test_queue.get_nowait()
            if OperationEvaluator.is_operator(cur_node._value):
                if cur_node._left_child is None or cur_node._right_child is None:
                    return False
                test_queue.put_nowait(cur_node._right_child)
                test_queue.put_nowait(cur_node._left_child)
            else:
                if cur_node._left_child is not None or cur_node._right_child is not None:
                    return False
        
        return True
    
    def evaluate_tree(self) -> float:
        if not self.is_tree_valid():
            raise OperationTreeEvaluationError("Tried to evaluate an invalid operation tree!")
        eval_stack = LifoQueue()
        eval_stack.put_nowait(self._root)

        operation_stack = LifoQueue()
        number_stack = LifoQueue()

        while not eval_stack.empty():
            cur_node: OperationTreeNode = eval_stack.get_nowait()
            if OperationEvaluator.is_operator(cur_node._value):
                operation_stack.put_nowait(cur_node._value)
                eval_stack.put_nowait(cur_node._left_child)
                eval_stack.put_nowait(cur_node._right_child)
            else:
                operation_stack.put_nowait(float(cur_node._value))
        
        while not operation_stack.empty():
            operation = operation_stack.get_nowait()
            if OperationEvaluator.is_operator(operation):
                # Because of shuffling between stacks, the operand order gets swapped.
                second_operand = number_stack.get_nowait()
                first_operand = number_stack.get_nowait()
                number_stack.put_nowait(OperationEvaluator.evaluate_operator(operation, first_operand, second_operand))
            else:
                number_stack.put_nowait(operation)
        
        return number_stack.get_nowait()
    
    def is_tree_valid_recursive(self) -> bool:
        return self._is_tree_valid_recursive_helper(self._root)

    def _is_tree_valid_recursive_helper(self, cur_node: OperationTreeNode) -> bool:
        if OperationEvaluator.is_operator(cur_node._value):
            if cur_node._left_child is None or not self._is_tree_valid_recursive_helper(cur_node._left_child):
                return False
            elif cur_node._right_child is None or not self._is_tree_valid_recursive_helper(cur_node._right_child):
                return False
        else:
            if cur_node._left_child is not None or cur_node._right_child is not None:
                return False
        return True

    def evaluate_tree_recursive(self) -> float:
        if not self.is_tree_valid_recursive():
            raise OperationTreeEvaluationError("Tried to evaluate an invalid operation tree!")
        return self._evaluate_tree_recursive_helper(self._root)
    
    def _evaluate_tree_recursive_helper(self, cur_node: OperationTreeNode) -> float:
        if OperationEvaluator.is_operator(cur_node._value):
            first_operand = self._evaluate_tree_recursive_helper(cur_node._left_child)
            second_operand = self._evaluate_tree_recursive_helper(cur_node._right_child)
            return OperationEvaluator.evaluate_operator(cur_node._value, first_operand, second_operand)
        
        return float(cur_node._value)
