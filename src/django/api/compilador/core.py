from . import lexico
from . import sintatico
from . import semantico
from . import solver

def getResponse(data):
    expression = data['content']

    print(expression)

    analisador_lexico = lexico.Lexic()
    analisador_semantico = semantico.Semantic()
    analisador_sintatico = sintatico.Sintatic(analisador_semantico)
    solucionador = solver.Solver()

    try:
        print('Analisando o lexico...')
        tokens = analisador_lexico.check(expression)
    except Exception as e:
        return str(e)

    print('Analisando o sintatico...')
    result = analisador_sintatico.check(tokens)

    if result == True:
        print('Calculando...')
        solution = solucionador.simplify(analisador_sintatico.factory.abs_tree[0])

        return str(solution)

    return result