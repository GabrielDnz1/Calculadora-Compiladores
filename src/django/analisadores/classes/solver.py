from sympy import *
import math
import factory as factory
from exp_enum import Exp

class Solver:
    def __init__(self):
        pass

    def simplify(self, expression):
        if expression.get_type() == Exp.BINARY_OP:
            op = expression.get_operation()

            # Simplifica os termos
            expression.e1 = self.simplify(expression.e1)
            expression.e2 = self.simplify(expression.e2)

            if op == '+':
                return expression.e1 + expression.e2
            elif op == '-':
                return expression.e1 - expression.e2
            elif op == '*':
                return expression.e1 * expression.e2
            elif op == '/':
                return expression.e1 / expression.e2
            elif op == '^':
                return expression.e1 ** expression.e2
            elif op == '=':
                return solve(Eq(expression.e1, expression.e2))
        elif expression.get_type() == Exp.UNARY_OP:
            op = expression.get_operation()

            # Simplifica o termo
            expression.expression = self.simplify(expression.expression)

            if op == '-':
                return expression.expression * -1
            
        elif expression.get_type() == Exp.CONSTANT:
            return expression.get_value()
        elif expression.get_type() == Exp.VARIABLE:
            var = symbols(expression.get_base())
            coefficient = expression.get_coefficient().get_value()
            exp = expression.get_exp().get_value()
            
            if coefficient != 1:
                var *= coefficient
            
            if exp != 1:
                var = var ** exp
            
            return var
        elif expression.get_type() == Exp.FUNCTION:
            func = expression.get_function()
            parameters = expression.get_parameters()
            ##print(parameters)

            for i in range(len(parameters)):
                parameters[i] = self.simplify(parameters[i])

            if func == 'log':
                return log(parameters[0], parameters[1])
            elif func == 'ln':
                return log(parameters[0])
            elif func == 'sin':
                return sin(parameters[0])
            elif func == 'cos':
                return cos(parameters[0])
            elif func == 'tan':
                return tan(parameters[0])

        return expression