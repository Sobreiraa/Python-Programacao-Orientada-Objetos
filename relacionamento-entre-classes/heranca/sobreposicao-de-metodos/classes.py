class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclass = self.__class__.__name__
    
    def falar(self):
        print(f'{self.nomeclass} está falando...')
    
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclass} está comprando...')
    
    def falar(self):
        print('Estou em CLIENTE.')

class ClienteVip(Cliente):
    # Chamando o construtor da super classe
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome 


    def falar(self):
        # super().falar() # Chamando o método da super classe.
        Pessoa.falar(self) # Chamando a instância de uma classe especifica
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')