"""
[Lexico]

Variáveis: apenas uma letra

Constantes: números sem sinais

Operadores: + - * / ^ =

Letra grega: alpha, beta, gamma, delta, elipson, zeta, eta, theta, iota, kappa, lambda, mu, nu, xi, omikron, pi, rho, sigma, tau, upsilon, phi, chi, psi, omega

Funções: log, cos, sen, tg

Delimitadores: ( ) ,

"""

letters = {'alpha', 'beta', 'gamma', 'delta', 'elipson', 'zeta', 'eta', 'theta', 'iota', 'kappa', 
                  'lambda', 'mu', 'nu', 'xi', 'omikron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 
                  'chi', 'psi', 'omega'}

functions = {'sin', 'cos', 'tan', 'ln', 'log'}

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
            elif char in {' ', '\t', '\0'}:
                pass
            elif char in {'(', ')', ','}:
                self.symbol += char
                self.current_state = 'q7'
            else:
                self.current_state = 'invalid'
        elif self.current_state == 'q1':
            if char == '.':
                self.symbol += char
                self.current_state = 'q2'
            elif char.isdigit():
                self.symbol += char
            else:
                self.reset('CONSTANTE')
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
                self.reset('CONSTANTE')
                self.transition(char)
        elif self.current_state == 'q4':
            if char.isalpha():
                self.symbol += char
                self.current_state = 'q5'
            else:
                self.reset('VARIAVEL')
                self.transition(char)
        elif self.current_state == 'q5':
            if char.isalpha():
                self.symbol += char
            else:
                if self.symbol in letters:
                    self.reset('VARIAVEL')
                    self.transition(char)
                elif self.symbol in functions:
                    self.reset('FUNCAO')
                    self.transition(char)
                else:
                    self.current_state = 'invalid'
        elif self.current_state == 'q6':
            self.reset('OPERADOR')
            self.transition(char)
        elif self.current_state == 'q7':
            self.reset('DELIMITADOR')
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
                raise Exception(f'Caractere \'{char}\' inválido!')

        self.symbols_table.append(('EOF', 'EOF'))
        return self.symbols_table
        ##for tuple in self.symbols_table:
            ##print("{:<5} {:<10}".format(*tuple))