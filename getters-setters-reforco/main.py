# SETTER = CONFIGURANDO UM VALOR (=)
# GETTER = OBTER UM VALOR (.)

class Pessoa:

    def __init__(self):
        self._nome = 'inicial'

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

p1 = Pessoa()
p1.nome = 'João'
print(p1.nome)
