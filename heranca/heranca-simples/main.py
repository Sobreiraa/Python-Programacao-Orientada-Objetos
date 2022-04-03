from classes import Pessoa, Cliente, Aluno

'''
Associação - USA | Agregação - TEM | Composição - É DONO | Herança - É
'''
c1 = Cliente('Matheus', 21)
c1.falar()
c1.comprar()

a1 = Aluno('Maria', 22)
a1.falar()
a1.estudar()