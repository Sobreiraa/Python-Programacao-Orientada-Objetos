from classes import Cliente, Endereco

cliente1 = Cliente('Matheus', 21)
cliente1.insere_enderecos('Anápolis', 'GO')
print(cliente1.nome)
cliente1.lista_ederecos()
del cliente1
print()


cliente2 = Cliente('Maria', 21)
cliente2.insere_enderecos('Osasco', 'SP')
cliente2.insere_enderecos('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_ederecos()
del cliente2
print()

cliente3 = Cliente('João', 22)
cliente3.insere_enderecos('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_ederecos()
del cliente3
print()

print('**********AQUI TERMINA O CODIGO***********')
