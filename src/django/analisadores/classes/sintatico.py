import factory

class Sintatic:
    def __init__(self, semantico):
        self.tokens = []
        self.current_token = (None, None)
        self.stack_pos = 0
        self.factory = factory.Factory()

        self.semantico = semantico

    def next(self):
        ##print(self.current_token[0])
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
            print(f'[ERRO] Erro sintático, {e}, encontrado: \'{self.tokens[self.stack_pos][0]}\'')
            return False
        
        if self.stack_pos != len(self.tokens):
            print(f'[ERRO] Erro sintático, encontrado: \'{self.tokens[self.stack_pos][0]}\'')
            return False
    
        return True
    
    """
    [Sintático]

    equacao -> expressão = expressão

    expressão -> termo expressão'| sinal termo expressão'
    expressão' -> operador_aditivo termo expressão' | e

    termo -> fator termo'
    termo' -> operador_multiplicativo fator termo' | e

    fator -> base ^ potência

    base -> variavel | constante variavel | constante | funcao(lista_de_parametros) | (expressão)

    potência -> constante

    lista_de_parametros -> parametro lista_de_parametros'
    lista_de_parametros' -> , parametro lista_de_parametros' | e

    parametro -> constante

    """

    def parser(self):
        self.expressao()

        if self.current_token[0] == '=':
            self.semantico.isEquation()
            self.next()

            self.expressao()

            self.semantico.check_equation()

            size = len(self.factory.abs_tree) - 1
            self.factory.create_binary_expression('=', self.factory.abs_tree[size-1], self.factory.abs_tree[size])

        if self.current_token[1] == 'EOF':
            self.next()

    def expressao(self):
        if self.current_token[0] == '+':
            self.next()
            self.termo()
        elif self.current_token[0] == '-':
            self.next()
            self.termo()
            self.factory.create_unary_expression('-', self.factory.abs_tree[len(self.factory.abs_tree) - 1])
        else:
            self.termo()

        self.expressao_2()

    def expressao_2(self):
        if self.current_token[0] in {'+', '-'}:
            op = self.current_token[0]
            self.next()

            self.termo()

            size = len(self.factory.abs_tree) - 1
            self.factory.create_binary_expression(op, self.factory.abs_tree[size-1], self.factory.abs_tree[size])

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
            
            size = len(self.factory.abs_tree) - 1
            self.factory.create_binary_expression('*', self.factory.abs_tree[size-1], self.factory.abs_tree[size])

        elif self.current_token[0] == '/':
            self.next()

            try:
                self.termo()
            except SyntaxError as e:
                if str(e) == '':
                    raise SyntaxError('esperado fator')
                else:
                    raise SyntaxError(e)
            
            size = len(self.factory.abs_tree) - 1
            self.factory.create_fraction(self.factory.abs_tree[size-1], self.factory.abs_tree[size])
            
    def fator(self):
        self.base()

        if self.current_token[0] == '^':
            self.next()
            self.potencia()

    def base(self):
        if self.current_token[1] == 'VARIAVEL':
            self.semantico.check_variable(self.current_token[0])
            self.factory.create_variable(self.current_token[0])
            ##print(self.abs_tree)
            self.next()
        elif self.current_token[1] == 'CONSTANTE':
            self.factory.create_constant(self.current_token[0])
            ##print(self.abs_tree)
            self.next()

            """
            if self.current_token[1] == 'VARIAVEL':
                self.semantico.check_variable(self.current_token[0])
                self.factory.create_variable(self.current_token[0])
                ##print(self.abs_tree)
                size = len(self.factory.abs_tree) - 1
                self.factory.create_binary_expression('*', self.factory.abs_tree[size-1], self.factory.abs_tree[size])
                self.next()
            """
        elif self.current_token[1] == 'FUNCAO':
            funcao = self.current_token[0]
            self.next()

            if self.current_token[0] != '(':
                raise SyntaxError('esperado \'(\'')
            
            self.next()

            self.lista_de_parametros()

            self.semantico.check_parameters(funcao)

            if self.current_token[0] != ')':
                raise SyntaxError('esperado \')\'')
            
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
        if self.current_token[1] != 'CONSTANTE':
            raise SyntaxError('esperado uma constante')

        self.factory.create_constant(self.current_token[0])
        ##print(self.abs_tree)
        size = len(self.factory.abs_tree) - 1
        self.factory.create_binary_expression('^', self.factory.abs_tree[size-1], self.factory.abs_tree[size])
        self.next()
    
    def lista_de_parametros(self):
        if self.current_token[1] != 'CONSTANTE':
            raise SyntaxError('esperado uma constante')
        
        self.next()

        self.semantico.parameters += 1

        if self.current_token[0] == ',':
            self.next()

            self.lista_de_parametros()