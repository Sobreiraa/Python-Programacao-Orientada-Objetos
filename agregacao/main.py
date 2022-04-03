from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()
p1 = Produto('Camisa', 50)
p2 = Produto('Chocolate', 4.50)
p3 = Produto('Tablet', 550)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p1)

carrinho.lista_produto()
print(carrinho.soma_total())