from .exp_enum import Exp

class Semantic:

    def __init__(self):
        self.constant = False
        self.variables = []
    
    def check_variable(self, token):
        if token not in self.variables:
            self.variables.append(token)

        if len(self.variables) > 1:
            raise Exception('Mais de uma variável foi encontrada')
    
    def check_parameters(self, function, parameters):
        size = len(parameters)

        if function == 'log':
            if size != 2:
                raise Exception('A função \'log\' precisa de dois parâmetros')
            
            if not self.check_parameter(parameters[0], Exp.CONSTANT) or not self.check_parameter(parameters[1], Exp.CONSTANT):
                raise Exception('A função \'log\' só aceita constantes')
        elif function in {'sin', 'cos', 'tan', 'ln'}:
            if size != 1:
                raise Exception(f'A função \'{function}\' precisa de um parâmetro')

            if not self.check_parameter(parameters[0], Exp.CONSTANT):
                raise Exception(f'A função \'{function}\' só aceita constante')
        elif function == '√':
            if size != 1:
                raise Exception('A função \'raíz quadrada\' precisa de um parâmetro')
        elif function == '\'':
            '''
            if size != 2:
                raise Exception('A função \'derivada\' precisa de dois parâmetros')
            
            if not self.check_parameter(parameters[1], Exp.VARIABLE):
                raise Exception('A função \'derivada\' precisa saber qual vai ser a variavel derivada')
            '''
            if size >= 0:
                raise Exception('Por enquanto a função \'derivada\' está inutilizável')
        elif function == '∫' or function == 'lim':
            if size >= 0:
                raise Exception('Por enquanto a função \'integral\' está inutilizável')
        
    def check_parameter(self, parameter, type):
        if parameter.get_type() == type:
            return True
        
        if parameter.get_type() == Exp.BINARY_OP:
            b1 = self.check_parameter(parameter.e1, type)
            b2 = self.check_parameter(parameter.e2, type)

            return b1 and b2
        
        if parameter.get_type() == Exp.UNARY_OP:
            return self.check_parameter(parameter.expression, type)
        
        if parameter.get_type() == Exp.FUNCTION:
            for p in parameter.parameters:
                if not self.check_parameter(p, type):
                    return False
            
            return True

        return False
        
    def check_equation(self):
        if len(self.variables) == 0:
            raise Exception(f'A equação não tem variáveis') 