from .exp_enum import Exp

class Expression:
    def __init__(self, type):
        self.type = type
    
    def get_type(self):
        return self.type

class Function(Expression):
    def __init__(self, func, parameters):
        super().__init__(Exp.FUNCTION)
        self.func = func
        self.parameters = parameters

    def get_function(self):
        return self.func
    
    def get_parameters(self):
        return self.parameters

class Constant(Expression):
    def __init__(self, value, constant_type):
        super().__init__(Exp.CONSTANT)
        self.value = value
        self.constant_type = constant_type
    
    def get_value(self):
        if self.constant_type == 'NATURAL':
            return int(self.value)
        else:
            return float(self.value)
    
class Variable(Expression):
    def __init__(self, base, exp, coefficient):
        super().__init__(Exp.VARIABLE)
        self.base = base
        self.exp = exp
        self.coefficient = coefficient
    
    def get_base(self):
        return self.base

    def get_coefficient(self):
        return self.coefficient
    
    def get_exp(self):
        return self.exp
                
class Operation(Expression):
    def __init__(self, type, operation):
        super().__init__(type)
        self.operation = operation
    
    def get_operation(self):
        return self.operation

class BinaryOperation(Operation):
    def __init__(self, operation, e1, e2):
        super().__init__(Exp.BINARY_OP, operation)
        self.e1 = e1
        self.e2 = e2

class UnaryOperation(Operation):
    def __init__(self, operation, expression):
        super().__init__(Exp.UNARY_OP, operation)
        self.expression = expression

class Factory:
    def __init__(self):
        self.abs_tree = []
        self.parameters = []
        self.constants = 0

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
        variable = Variable(variable, Constant(1, 'NATURAL'), Constant(1, 'NATURAL'))
        self.abs_tree.append(variable)
    
    def create_constant(self, constant, constant_type):
        constant  = Constant(constant, constant_type)
        self.abs_tree.append(constant)

    def create_function(self, func):
        function = Function(func, self.parameters.copy())
        self.abs_tree.append(function)
        self.parameters.clear()
    
    def create_parameter(self, parameter):
        self.parameters.append(parameter)
    
    def reduce_constants(self):
        for i in range(self.constants):
            self.create_binary_expression('*', self.abs_tree[-2], self.abs_tree[-1])
        
        self.constants = 0