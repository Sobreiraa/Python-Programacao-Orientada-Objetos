'''
Uma exceção (exception) é um objeto especial, de uma classe específica que é destinada a sinalização de situações que podem ser tratadas pelo programador.

Isto significa que uma exceção indica a ocorrência de uma anormalidade no código, a qual poderia ser solucionada pelo próprio programa, por meio do uso de um dado alternativo, de uma outra estratégia de cálculo, pela obtenção de um novo dado junto ao usuário do programa, ou eventualmente outra ação considerada apropriada
'''

from logging import exception


class TaErradoError(Exception):
    pass

def testar():
    raise TaErradoError('Errado.')

try:
    testar()
except TaErradoError as error:
    print(F'Erro: {error}')