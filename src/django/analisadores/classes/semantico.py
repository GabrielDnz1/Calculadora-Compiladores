class Semantic:

    def __init__(self):
        self.buffer = None
        self.variables = []
    
    def check_variable(self, token):
        if token not in self.variables:
            self.variables.append(token)

        if len(self.variables) > 1:
            raise Exception('Mais de uma variável foi encontrada')
    
    def check_parameters(self, funcao, size):
        if funcao == 'log' and size != 2:
            raise Exception('A função Log precisa de dois parâmetros')
        elif funcao in {'sin', 'cos', 'tan', 'ln'} and size != 1:
            raise Exception(f'A função {funcao} precisa de um parâmetro')
    
    def check_equation(self):
        if len(self.variables) == 0:
            raise Exception(f'A equação não tem variáveis') 