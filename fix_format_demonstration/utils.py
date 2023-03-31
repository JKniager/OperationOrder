class OperatorFuncs:

    @classmethod
    def addition(self, first_operand: float, second_operand: float) -> float:
        return first_operand + second_operand
    
    @classmethod
    def subtraction(self, first_operand: float, second_operand: float) -> float:
        return first_operand - second_operand
    
    @classmethod
    def multiplication(self, first_operand: float, second_operand: float) -> float:
        return first_operand * second_operand
    
    @classmethod
    def division(self, first_operand: float, second_operand: float) -> float:
        return first_operand / second_operand

    @classmethod
    def power(self, first_operand: float, second_operand: float) -> float:
        return first_operand ** second_operand


class OperationEvaluator:
    OPERATOR_LOOKUP_TABLE = {
        '+' : OperatorFuncs.addition,
        '-' : OperatorFuncs.subtraction,
        '*' : OperatorFuncs.multiplication,
        '/' : OperatorFuncs.division,
        '^' : OperatorFuncs.power
    }

    ORDER_OF_OPERATIONS = {
        '^' : 0,
        '*' : 1,
        '/' : 1,
        '+' : 2,
        '-' : 2
    }

    @classmethod
    def is_operator(self, operator: str):
        return operator in OperationEvaluator.OPERATOR_LOOKUP_TABLE
    
    @classmethod
    def compare_operator_order(self, first_operator, second_operator) -> bool:
        '''Checks if first_operator should be performed before second_operator
        when evaluating an expression. Order of operations is mainly used for
        expression formats which use parentheses, like in-fix.
        '''
        return self.ORDER_OF_OPERATIONS[first_operator] <= self.ORDER_OF_OPERATIONS[second_operator]
    
    @classmethod
    def evaluate_operator(self, operator: str, first_operand: float, second_operand: float):
        if OperationEvaluator.is_operator(operator):
            return OperationEvaluator.OPERATOR_LOOKUP_TABLE[operator](first_operand, second_operand)

        return None
