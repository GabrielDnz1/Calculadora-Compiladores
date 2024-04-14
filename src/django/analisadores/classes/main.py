import lexico
import sintatico
import semantico
##import solver

result = True

while(result):
    exp = input('digite a expressão: ')

    analisador_lexico = lexico.Lexic()
    analisador_semantico = semantico.Semantic()
    analisador_sintatico = sintatico.Sintatic(analisador_semantico)
    ##solucionador = solver.Solver()

    try:
        tokens = analisador_lexico.check(exp)
    except Exception as e:
        print(e)
        break

    result = analisador_sintatico.check(tokens)
    print(result)

    """
    if result:
        solucionador.setConfig(analisador_sintatico.semantico.flags)
        
        solution = solucionador.solve(analisador_sintatico.factory.abs_tree[0])

        print(solution)
    """