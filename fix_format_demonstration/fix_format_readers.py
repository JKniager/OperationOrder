from .operation_tree import OperationTreeNode, OperationTree
import queue
from queue import LifoQueue
from .utils import OperationEvaluator


class InvalidInfixExpressionError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def infix_to_operation_tree(equation: str, sep: str = " ") -> OperationTree:
    if len(equation) == 0:
        raise InvalidInfixExpressionError("Empty expression!")

    split_equ = equation.split(sep=sep)
    operator_stack = LifoQueue()
    node_stack = LifoQueue()
    expecting_number = True

    for i in split_equ:
        if OperationEvaluator.is_operator(i):
            if expecting_number:
                raise InvalidInfixExpressionError(f"Expression '{equation}' is misformatted!")
            # Make sure there aren't any operations we have to perform before the current operator 'i'.
            while not operator_stack.empty():
                test_operator = operator_stack.get_nowait()
                if test_operator == '(' or not OperationEvaluator.compare_operator_order(test_operator, i):
                    operator_stack.put_nowait(test_operator)
                    break
                else:
                    second_operand = None
                    first_operand = None
                    try:
                        second_operand = node_stack.get_nowait()
                        first_operand = node_stack.get_nowait()
                    except queue.Empty:
                        raise InvalidInfixExpressionError(f"Expression '{equation}' is missing an operand!")
                    new_node = OperationTreeNode(test_operator, None)
                    new_node.setLeft(first_operand)
                    new_node.setRight(second_operand)
                    node_stack.put_nowait(new_node)
            operator_stack.put_nowait(i)
            expecting_number = True
        elif i == '(':
            if not expecting_number:
                raise InvalidInfixExpressionError(f"Expression '{equation}' is misformatted!")
            operator_stack.put_nowait(i)
        elif i == ')':
            if expecting_number:
                raise InvalidInfixExpressionError(f"Expression '{equation}' is misformatted!")
            test_operator = ''
            try:
                test_operator = operator_stack.get_nowait()
            except queue.Empty:
                raise InvalidInfixExpressionError(f"Expression '{equation}' is missing a '('!")
            while test_operator != '(':
                second_operand = None
                first_operand = None
                try:
                    second_operand = node_stack.get_nowait()
                    first_operand = node_stack.get_nowait()
                except queue.Empty:
                    raise InvalidInfixExpressionError(f"Expression '{equation}' is missing an operand!")
                new_node = OperationTreeNode(test_operator, None)
                new_node.setLeft(first_operand)
                new_node.setRight(second_operand)
                node_stack.put_nowait(new_node)
                try:
                    test_operator = operator_stack.get_nowait()
                except queue.Empty:
                    raise InvalidInfixExpressionError(f"Expression '{equation}' is missing a '('!")
        else:
            if not expecting_number:
                raise InvalidInfixExpressionError(f"Expression '{equation}' is misformatted!")
            node_stack.put_nowait(OperationTreeNode(i, None))
            expecting_number = False
    
    while not operator_stack.empty():
        operator = operator_stack.get_nowait()
        if operator == '(':
            raise InvalidInfixExpressionError(f"Expression '{equation}' is missing a ')'!")

        second_operand = None
        first_operand = None
        try:
            second_operand = node_stack.get_nowait()
            first_operand = node_stack.get_nowait()
        except queue.Empty:
            raise InvalidInfixExpressionError(f"Expression '{equation}' is missing an operand!")
        new_node = OperationTreeNode(operator, None)
        new_node.setLeft(first_operand)
        new_node.setRight(second_operand)
        node_stack.put_nowait(new_node)
    
    if node_stack.qsize() > 1:
        raise InvalidInfixExpressionError(f"Expression '{equation}' has an extra operand!")

    return OperationTree(node_stack.get_nowait())



def calculate_infix(equation: str, sep: str = " ") -> float:
    '''Parse an expression in in-fix format, and return the calculated result.
    '''
    if len(equation) == 0:
        return 0.0

    split_equ = equation.split(sep=sep)
    operator_stack = LifoQueue()
    number_stack = LifoQueue()

    expecting_number = True
    for i in split_equ:
        if OperationEvaluator.is_operator(i):
            if expecting_number:
                raise InvalidInfixExpressionError(f"Expression '{equation}' is misformatted!")
            # Make sure there aren't any operations we have to perform before the current operator 'i'.
            while not operator_stack.empty():
                test_operator = operator_stack.get_nowait()
                if test_operator == '(' or not OperationEvaluator.compare_operator_order(test_operator, i):
                    operator_stack.put_nowait(test_operator)
                    break
                else:
                    second_operand = None
                    first_operand = None
                    try:
                        second_operand = number_stack.get_nowait()
                        first_operand = number_stack.get_nowait()
                    except queue.Empty:
                        raise InvalidInfixExpressionError(f"Expression '{equation}' is missing an operand!")
                    number_stack.put_nowait(OperationEvaluator.evaluate_operator(test_operator, first_operand, second_operand))
            operator_stack.put_nowait(i)
            expecting_number = True
        elif i == '(':
            if not expecting_number:
                raise InvalidInfixExpressionError(f"Expression '{equation}' is misformatted!")
            operator_stack.put_nowait(i)
        elif i == ')':
            if expecting_number:
                raise InvalidInfixExpressionError(f"Expression '{equation}' is misformatted!")
            test_operator = ''
            try:
                test_operator = operator_stack.get_nowait()
            except queue.Empty:
                raise InvalidInfixExpressionError(f"Expression '{equation}' is missing a '('!")
            while test_operator != '(':
                second_operand = None
                first_operand = None
                try:
                    second_operand = number_stack.get_nowait()
                    first_operand = number_stack.get_nowait()
                except queue.Empty:
                    raise InvalidInfixExpressionError(f"Expression '{equation}' is missing an operand!")
                number_stack.put_nowait(OperationEvaluator.evaluate_operator(test_operator, first_operand, second_operand))
                try:
                    test_operator = operator_stack.get_nowait()
                except queue.Empty:
                    raise InvalidInfixExpressionError(f"Expression '{equation}' is missing a '('!")
        else:
            if not expecting_number:
                raise InvalidInfixExpressionError(f"Expression '{equation}' is misformatted!")
            number_stack.put_nowait(float(i))
            expecting_number = False
    
    while not operator_stack.empty():
        operator = operator_stack.get_nowait()
        if operator == '(':
            raise InvalidInfixExpressionError(f"Expression '{equation}' is missing a ')'!")

        second_operand = None
        first_operand = None
        try:
            second_operand = number_stack.get_nowait()
            first_operand = number_stack.get_nowait()
        except queue.Empty:
            raise InvalidInfixExpressionError(f"Expression '{equation}' is missing an operand!")
        number_stack.put_nowait(OperationEvaluator.evaluate_operator(operator, first_operand, second_operand))
    
    if number_stack.qsize() > 1:
        raise InvalidInfixExpressionError(f"Expression '{equation}' has an extra operand!")

    return number_stack.get_nowait()


class InvalidPostfixExpressionError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def postfix_to_operation_tree(equation: str, sep: str = " ") -> OperationTree:
    if len(equation) == 0:
        raise InvalidPostfixExpressionError("Empty expression!")

    split_equ = equation.split(sep=sep)

    stack = LifoQueue()

    for i in split_equ:
        cur_node = OperationTreeNode(i, None)
        if OperationEvaluator.is_operator(i):
            try:
                cur_node.setRight(stack.get_nowait())
                cur_node.setLeft(stack.get_nowait())
            except queue.Empty:
                raise InvalidPostfixExpressionError(f"Expression '{equation}' has a dangling operator!")
        stack.put_nowait(cur_node)
    
    if stack.qsize() > 1:
        raise InvalidPostfixExpressionError(f"Expression '{equation}' has an extra operand!")
    
    return OperationTree(stack.get_nowait())


def calculate_postfix(equation: str, sep: str = " ") -> float:
    '''Parse an expression in post-fix format, and return the calculated result.
    '''
    if len(equation) == 0:
        return 0.0

    split_equ = equation.split(sep=sep)

    # A valid post-fix expression should always end in an operator.
    if not OperationEvaluator.is_operator(split_equ[-1]):
        raise InvalidPostfixExpressionError(f"Expression: '{equation}' has an extra operand!")

    lq = LifoQueue()
    for i in split_equ:
        if OperationEvaluator.is_operator(i):
            try:
                second_arg = lq.get_nowait()
                first_arg = lq.get_nowait()
                lq.put_nowait(OperationEvaluator.evaluate_operator(i, first_arg, second_arg))
            except queue.Empty:
                # If we don't have any numbers on the stack, then this is an extra operator.
                raise InvalidPostfixExpressionError(f"Expression: '{equation}' has a dangling operator!")
        else:
            lq.put_nowait(float(i))
    
    if lq.qsize() > 1:
        raise InvalidPostfixExpressionError(f"Expression: '{equation}' has an extra operand!")

    return lq.get_nowait()


class InvalidPrefixExpressionError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def prefix_to_operation_tree(equation: str, sep: str = " ") -> OperationTree:
    if len(equation) == 0:
        return 0.0

    split_equ = equation.split(sep=sep)

    cur_node = OperationTreeNode(split_equ[0], None)
    tree = OperationTree(cur_node)

    for i in split_equ[1:]:
        while cur_node._parent is not None and cur_node._left_child is not None and cur_node._right_child is not None:
                cur_node = cur_node._parent
        if cur_node._left_child is None:
            cur_node.setLeft(OperationTreeNode(i, cur_node))
            if OperationEvaluator.is_operator(i):
                cur_node = cur_node._left_child
        elif cur_node._right_child is None:
            cur_node.setRight(OperationTreeNode(i, cur_node))
            if OperationEvaluator.is_operator(i):
                cur_node = cur_node._right_child
    
    if not tree.is_tree_valid():
        raise InvalidPrefixExpressionError()
    
    return tree


def calculate_prefix(equation: str, sep: str = " ") -> float:
    '''Parse an expression in pre-fix format, and return the calculated result.
    '''
    if len(equation) == 0:
        return 0.0

    # An expression in pre-fix format can be reversed and calculated in a similar manner to expressions in post-fix format.
    # Note that there are slight alterations to the process since reversing everything also changes the position of
    # the operands, which our code must account for.
    split_equ = equation.split(sep=sep)
    split_equ.reverse()

    # A valid post-fix expression should always start with an operator.
    if not OperationEvaluator.is_operator(split_equ[-1]):
        raise InvalidPrefixExpressionError(f"Expression: '{equation}' has an extra operand!")

    lq = LifoQueue()
    for i in split_equ:
        if OperationEvaluator.is_operator(i):
            try:
                # Notice that unlike post-fix, the first operand comes before the second operand in the stack.
                # This is because the stack has a reversing effect on the order of items put into it.
                # Since we already reversed the sequence above, the stack undoes our reversal of the operands.
                first_arg = lq.get_nowait()
                second_arg = lq.get_nowait()
                lq.put_nowait(OperationEvaluator.evaluate_operator(i, first_arg, second_arg))
            except queue.Empty:
                # If we don't have any numbers on the stack, then this is an extra operator.
                raise InvalidPrefixExpressionError(f"Expression: '{equation}' has a dangling operator!")
        else:
            lq.put_nowait(float(i))
    
    if lq.qsize() > 1:
        raise InvalidPrefixExpressionError(f"Expression: '{equation}' has an extra operand!")

    return lq.get_nowait()
