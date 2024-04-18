from sympy import symbols
import math
import factory as factory
from exp_enum import Exp

class Solver:
    def __init__(self):
        self.flags = {"Equation": False}

    def setConfig(self, flags):
        self.flags = flags

    def solve(self, expression):
        if expression.get_type() == Exp.BINARY_OP:

            # Simplifica os termos
            if expression.e1.get_type() == Exp.BINARY_OP:
                expression.e1 = self.solve(expression.e1)
            
            if expression.e2.get_type() == Exp.BINARY_OP:
                expression.e2 = self.solve(expression.e2)

            # Realiza as operações
            if expression.get_operation() == '+':
                expression = self.add(expression.e1, expression.e2) or expression
            elif expression.get_operation() == '-':
                expression.e2.set_value(expression.e2.get_value()*-1) ## Risco de dar erro
                expression = self.add(expression.e1, expression.e2) or expression
            elif expression.get_operation() == '*':
                expression = self.multiplicate(expression.e1, expression.e2) or expression
            elif expression.get_operation() == '^':
                expression = self.exponentiation(expression.e1, expression.e2) or expression

            return expression
    
    def add(self, e1, e2):
        #print(e1.get(), e1.get_type(), e2.get(), e2.get_type())
        # Ex: 2+2 = 4
        if e1.get_type() == e2.get_type() == Exp.CONSTANT:  # Isso só suporta números racionais
            e1.set_value(e1.get_value() + e2.get_value())

            return e1
        
        # Ex: x+x = 2x
        if e1.get_type() == e2.get_type() == Exp.VARIABLE: # Quebra se a expressão tem duas variáveis
            if e1.get_exp().get_value() == e2.get_exp().get_value():
                e1.set_coefficient(self.add(e1.get_coefficient(), e2.get_coefficient()))

                return e1
            
        # Ex: x+2+x = 2x+2
        if e1.get_type() == Exp.BINARY_OP:
            result = self.add(e1.e1, e2)

            if result != False:
                e1.e1 = result
                return e1
            
            result = self.add(e1.e2, e2)

            if result != False:
                e1.e2 = result
                return e1

        return False
    
    def multiplicate(self, e1, e2):
        ##print(e1.get(), e1.get_type(),  e2.get(), e2.get_type())
        # Ex: 1*1 = 1
        if e1.get_type() == e2.get_type() == Exp.CONSTANT: # Isso só suporta números racionais
            e1.set_value(e1.get_value() * e2.get_value())

            return e1
        
        # Ex: x*2x = 2x^2
        if e1.get_type() == e2.get_type() == Exp.VARIABLE: # Quebra se a expressão tem duas variáveis
            e1.set_coefficient(self.multiplicate(e1.get_coefficient(), e2.get_coefficient()))
            e1.get_exp(e1.get_exp() + e2.get_exp())

            return e1
        
        # Ex: 3*2x = 6x
        if {e1.get_type(), e2.get_type()} == {Exp.CONSTANT, Exp.VARIABLE}:
            if e2.get_type() == Exp.CONSTANT:
                _temp = e1
                e1 = e2
                e2 = _temp

            e2.set_coefficient(self.multiplicate(e1, e2.get_coefficient()))
            
            return e2
        
        # Ex: 3*(x+2) = 3x+6 ou x*(x+2) = 2
        # Ainda a implementar...
        """
        if (e1.get_type() == Exp.BINARY_OP and e2.get_type() in (Exp.CONSTANT, Exp.VARIABLE)) or (e1.get_type() in (Exp.CONSTANT, Exp.VARIABLE) and e2.get_type() == Exp.BINARY_OP):
            if e2.get_type() == Exp.BINARY_OP:
                _temp = e1
                e1 = e2
                e2 = _temp
            
            print(e1.get(), e2.get())
            e1.e1 = self.multiplicate(e1.e1, e2)
            print(e1.get(), e2.get())
            e1.e2 = self.multiplicate(e1.e2, e2) 

            return e1
        """
            

        return False
    
    def exponentiation(self, e1, e2):
        ##print(e1.get(), e2.get())
        # Ex: 2^3 = 8
        if e1.get_type() == e2.get_type() == Exp.CONSTANT: ## Verificar dps casos com raízes
            e1.set_value(math.pow(e1.get_value(), e2.get_value()))

            return e1
        
        # Ex: x^2 = x²
        if e1.get_type() == Exp.VARIABLE and e2.get_type() == Exp.CONSTANT:
            e1.set_exp(self.multiplicate(e1.get_exp(), e2))

            return e1
        
        # Ex: (x+2)^2 = x^2+4x+4
        # Ainda a implementar...
        # Talvez usar a tecinca (a+b)^2 = (a+b)(a+b)?

        return False