'''
Em outras linguagens:
public, protected, private

convenções:
_ -> protected
__ -> private
'''

class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    
    # Estamos apenas tratando um dicionário como base de dados.
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]
    
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

bd = BaseDeDados()
bd.inserir_cliente(1, 'Matheus')
bd.inserir_cliente(2, 'Luana')
bd.inserir_cliente(3, 'Lucca')
bd.apaga_cliente(2)
bd.__dados = 'Outra coisa'
# print(bd.__dados)
# print(bd._BaseDeDados__dados)
# bd.lista_clientes()