from exp_enum import Exp

class Expression:
    def __init__(self, type):
        self.type = type
        self.simplify = True

    def set_simplify(self, bool):
        self.simplify = bool
    
    def can_simplify(self):
        return self.simplify
    
    def get_type(self):
        return self.type
    
    def get(self):
        pass

class Constant(Expression):
    def __init__(self, value):
        super().__init__(Exp.CONSTANT)
        self.value = value
        self.simplify = False
    
    def get_value(self):
        return float(self.value)
    
    def set_value(self, value):
        self.value = value

    def get(self):
        return float(self.value)
    
class Fraction(Expression):
    def __init__(self, e1, e2):
        super().__init__(Exp.FRACTION)
        self.numerator = e1
        self.denominator = e2
    
    def get_expressions(self):
        return self.numerator, self.denominator
    
    def get_numerator(self):
        return self.numerator
    
    def set_numerator(self, num):
        self.numerator = num
    
    def get_denominator(self):
        return self.denominator
    
    def set_denominator(self, den):
        self.denominator = den
    
    def get(self):
        pass

class Variable(Expression):
    def __init__(self, base, exp, coefficient):
        super().__init__(Exp.VARIABLE)
        self.base = base
        self.exp = exp
        self.coefficient = coefficient
        self.simplify = False
    
    def get_base(self):
        return self.base

    def get_coefficient(self):
        return self.coefficient

    def set_coefficient(self, coefficient):
        self.coefficient = coefficient
    
    def get_exp(self):
        return self.exp
    
    def set_exp(self, exp):
        self.exp = exp
    
    def get(self):
        coefficient = ''
        exp = ''

        if self.exp.get_value() != 1:
            exp = (f'^{self.exp.get_value()}')

        if self.coefficient.get_value() != 1:
            coefficient = self.coefficient.get_value()
            

        return (f'{coefficient}{self.base}{exp}') # Pode quebrar se exp não for constante
                
class Operation(Expression):
    def __init__(self, type, operation):
        super().__init__(type)
        self.operation = operation

class BinaryOperation(Operation):
    def __init__(self, operation, e1, e2):
        super().__init__(Exp.BINARY_OP, operation)
        self.e1 = e1
        self.e2 = e2
    
    def get_expressions(self):
        return self.e1, self.e2

    def get_operation(self):
        return self.operation

    def get(self):
        return (f'{self.e1.get()}{self.operation}{self.e2.get()}')

class UnaryOperation(Operation):
    def __init__(self, operation, expression):
        super().__init__(Exp.UNARY_OP, operation)
        self.expression = expression
    
    def get(self):
        return (f'{self.operation}{self.expression.get()}')

class Factory:
    def __init__(self):
        self.abs_tree = []

    def create_binary_expression(self, operation, e1, e2):
        op = BinaryOperation(operation, e1, e2)
        self.abs_tree.pop()
        self.abs_tree.pop()
        self.abs_tree.append(op)

    def create_unary_expression(self, operation, e):
        op = UnaryOperation(operation, e)
        self.abs_tree.pop()
        self.abs_tree.append(op)
    
    def create_variable(self, variable):
        variable = Variable(variable, Constant(1), Constant(1))
        self.abs_tree.append(variable)
    
    def create_constant(self, constant):
        constant  = Constant(constant)
        self.abs_tree.append(constant)
    
    def create_fraction(self, e1, e2):
        fraction = Fraction(e1, e2)
        self.abs_tree.pop()
        self.abs_tree.pop()
        self.abs_tree.append(fraction)