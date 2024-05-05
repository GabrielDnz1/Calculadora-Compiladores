from . import factory

class Sintatic:
    def __init__(self, semantico):
        self.tokens = []
        self.current_token = (None, None)
        self.stack_pos = 0
        self.factory = factory.Factory()

        self.semantico = semantico

    def next(self):
        self.stack_pos += 1
        self.current_token = self.tokens[self.stack_pos] if self.stack_pos < len(self.tokens) else (None, None)

    def check(self, tokens):
        self.tokens = tokens
        self.current_token = tokens[0]

        try:
            self.parser()
        except SyntaxError as e:
            if self.stack_pos == len(self.tokens):
                self.stack_pos -= 1
            return f'[ERRO] Erro sintático, {e}, encontrado: \'{self.tokens[self.stack_pos][0]}\''
        
        if self.stack_pos != len(self.tokens):
            return f'[ERRO] Erro sintático, encontrado: \'{self.tokens[self.stack_pos][0]}\''
    
        return True
    
    """
    [Sintático]

    texto -> sistema | equacao | expressão

    sistema -> { lista_de_equações }

    lista_de_equações -> equacao lista_de_equações'
    lista_de_equações' -> , equacao lista_de_equações

    equacao -> expressão = expressão

    expressão -> termo expressão'| sinal termo expressão'
    expressão' -> operador_aditivo termo expressão' | e

    termo -> fator termo'
    termo' -> operador_multiplicativo fator termo' | e

    fator -> constante lista_de_constantes expoente

    lista_de_constantes -> constante lista_de_constantes expoente | e

    expoente -> ^ potência | e

    constante -> funcao(lista_de_parametros) | num | variavel | (expressão)

    potência -> num 

    lista_de_parametros -> expressão lista_de_parametros'
    lista_de_parametros' -> , expressão lista_de_parametros' | e

    """

    def parser(self):
        self.expressao()

        if self.current_token[0] == '=':
            self.next()

            self.expressao()

            try:
                self.semantico.check_equation()
            except Exception as e:
                raise SyntaxError(e)

            self.factory.create_binary_expression('=', self.factory.abs_tree[-2], self.factory.abs_tree[-1])

        if self.current_token[1] == 'EOF':
            self.next()

    def expressao(self):
        if self.current_token[0] == '+':
            self.next()
            self.termo()
        elif self.current_token[0] == '-':
            self.next()
            self.termo()
            self.factory.create_unary_expression('-', self.factory.abs_tree[-1])
        else:
            self.termo()

        self.expressao_2()

    def expressao_2(self):
        if self.current_token[0] in {'+', '-'}:
            op = self.current_token[0]
            self.next()

            self.termo()

            self.factory.create_binary_expression(op, self.factory.abs_tree[-2], self.factory.abs_tree[-1])

            self.expressao_2()

    def termo(self):
        self.fator()

        if self.current_token[0] == '*':
            self.next()

            try:
                self.termo()
            except SyntaxError as e:
                if str(e) == '':
                    raise SyntaxError('esperado fator')
                else:
                    raise SyntaxError(e)
            
            self.factory.create_binary_expression('*', self.factory.abs_tree[-2], self.factory.abs_tree[-1])

        elif self.current_token[0] == '/':
            self.next()

            try:
                self.termo()
            except SyntaxError as e:
                if str(e) == '':
                    raise SyntaxError('esperado fator')
                else:
                    raise SyntaxError(e)
            
            self.factory.create_binary_expression('/', self.factory.abs_tree[-2], self.factory.abs_tree[-1])
            
    def fator(self):
        try:
            self.constante()
        except SyntaxError as e:
            if str(e) == '':
                raise SyntaxError('esperado fator')
            else:
                raise SyntaxError(e)

        self.lista_de_constantes()
        self.expoente()
    
    def expoente(self):
        if self.current_token[0] == '^':
            self.next()
            self.potencia()

    def lista_de_constantes(self):
        try:
            self.constante()
            self.lista_de_constantes()
            self.expoente()
            self.factory.create_binary_expression('*', self.factory.abs_tree[-2], self.factory.abs_tree[-1])
        except SyntaxError as e:
            if str(e) != '':
                raise SyntaxError(e)
            

    def constante(self):
        if self.current_token[1] == 'FUNCAO':
            funcao = self.current_token[0]
            self.next()

            if self.current_token[0] != '(':
                raise SyntaxError('esperado \'(\'')
            
            self.next()

            self.lista_de_parametros()

            if self.current_token[0] != ')':
                raise SyntaxError('esperado \')\'')
            
            try:
                self.semantico.check_parameters(funcao, self.factory.parameters)
            except Exception as e:
                raise SyntaxError(e)
            
            self.factory.create_function(funcao)
            
            self.next()
        elif self.current_token[1] in ('NATURAL', 'RACIONAL'):
            self.factory.create_constant(self.current_token[0], self.current_token[1])
            self.next()
        elif self.current_token[1] == 'VARIAVEL':
            try:
                self.semantico.check_variable(self.current_token[0])
            except Exception as e:
                raise SyntaxError(e)
            
            self.factory.create_variable(self.current_token[0])
            self.next()
        elif self.current_token[0] == '(':
            self.next()

            self.expressao()

            if self.current_token[0] != ')':
                raise SyntaxError('esperado \'(\'')
            
            self.next()
        else:
            raise SyntaxError('')
    
    def potencia(self):
        if self.current_token[1] not in ('NATURAL', 'RACIONAL'):
            raise SyntaxError('esperado uma potencia')

        self.factory.create_constant(self.current_token[0], self.current_token[1])
        ##print(self.abs_tree)
        self.factory.create_binary_expression('^', self.factory.abs_tree[-2], self.factory.abs_tree[-1])
        self.next()
    
    def lista_de_parametros(self):
        _copy1 = self.factory.abs_tree.copy()
        self.factory.abs_tree.clear()
        self.factory.parameters.clear()

        self.expressao()
        
        self.factory.create_parameter(self.factory.abs_tree[0])

        self.factory.abs_tree = _copy1.copy()
        _copy2 = self.factory.parameters.copy()

        if self.current_token[0] == ',':
            self.next()

            self.lista_de_parametros()
            _copy2.append(self.factory.parameters[0])

        self.factory.parameters = _copy2.copy()