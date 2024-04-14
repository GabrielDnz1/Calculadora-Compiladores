class Semantic:

    def __init__(self):
        self.buffer = None
        self.variables = []

        self.parameters = 0

        self.flags = {"Equation": False}
    
    def check_variable(self, token):
        if token in self.variables:
            self.variables.append(token)

        if len(self.variables) > 1:
            raise Exception('Mais de uma variável foi encontrada')
    
    def check_parameters(self, funcao):
        if funcao == 'log' and self.parameters != 2:
            raise Exception('A função Log precisa de dois parâmetros')
        elif funcao in {'sin', 'cos', 'tan', 'ln'} and self.parameters != 1:
            raise Exception(f'A função {funcao} precisa de um parâmetro')
        
        self.parameters = 0
    
    def check_equation(self):
        if len(self.variables) == 0:
            raise Exception(f'A equação não tem variáveis') 
    
    def isEquation(self):
        self.flags["Equation"] = True