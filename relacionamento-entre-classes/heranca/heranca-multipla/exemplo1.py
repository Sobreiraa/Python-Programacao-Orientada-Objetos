class A:
    def falar(self):
        print('Falando... Estou em A.')

class B(A):
    def falar(self):
        print('Falando... Estou em B.')

class C(A):
    def falar(self):
        print('Falando... Estou em C')

class D(B, C): # A ordem da herança múltipla vai da esquerda pra direita
    def falar(self):
        print('Falando... Estou em D.')

d = D()
d.falar()