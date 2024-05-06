functions = {'sin', 'cos', 'tg', 'ln', 'log', 'lim'}

class Lexic:
    def __init__(self):
        self.current_state = 'q0'
        self.symbol = ''
        self.symbols_table = []
    
    def transition(self, char):
        if self.current_state == 'q0':
            if char.isdigit():
                self.symbol += char
                self.current_state = 'q1'
            elif char.isalpha():
                self.symbol += char
                self.current_state = 'q4'
            elif char in {'+', '-', '/', '*', '^', '='}:
                self.symbol += char
                self.current_state = 'q6'
            elif char in {' ', '\t', '\0', '\n'}:
                pass
            elif char in {'(', ')', ','}:
                self.symbol += char
                self.current_state = 'q7'
            elif char in {"'", '∫', '√'}:
                self.symbol += char
                self.current_state = 'q8'
            else:
                self.current_state = 'invalid'
        elif self.current_state == 'q1':
            if char == '.':
                self.symbol += char
                self.current_state = 'q2'
            elif char.isdigit():
                self.symbol += char
            else:
                self.reset('NATURAL')
                self.transition(char)
        elif self.current_state == 'q2':
            if char.isdigit():
                self.symbol += char
                self.current_state = 'q3'
            else:
                self.current_state = 'invalid'
        elif self.current_state == 'q3':
            if char.isdigit():
                self.symbol += char
            else:
                self.reset('RACIONAL')
                self.transition(char)
        elif self.current_state == 'q4':
            if char.isalpha():
                self.symbol += char
                self.current_state = 'q5'
            else:
                self.reset('VARIAVEL')
                self.transition(char)
        elif self.current_state == 'q5':
            if self.symbol in functions:
                self.reset('FUNCAO')
                self.transition(char)
            elif char.isalpha():
                self.symbol += char
            else:
                self.current_state = 'invalid'
        elif self.current_state == 'q6':
            self.reset('OPERADOR')
            self.transition(char)
        elif self.current_state == 'q7':
            self.reset('DELIMITADOR')
            self.transition(char)
        elif self.current_state == 'q8':
            self.reset('FUNCAO')
            self.transition(char)

    def reset(self, classifier):
        self.current_state = 'q0'
        self.symbols_table.append((self.symbol, classifier))
        self.symbol = ''

    def check(self, line):
        line += '\0'

        for char in line:
            self.transition(char)

            if self.current_state == 'invalid':
                raise Exception(f'Caractere \'{char if self.symbol == '' else self.symbol}\' inválido!')

        
        self.symbols_table.append(('EOF', 'EOF'))
        return self.symbols_table