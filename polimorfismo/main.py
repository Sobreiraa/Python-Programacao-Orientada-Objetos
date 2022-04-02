from abc import ABC, abstractmethod

class A(ABC):
    def fala(self):
        pass

class B(A):
    def fala(self, msg):
        print(f'B está falando sobre {msg}')

class C(A):
    def fala(self, msg):
        print(f'C está falando sobre {msg}')
    
b = B()
c = C()

b.fala('Futebol')
c.fala('Música')