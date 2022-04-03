'''
No python, o comportamento dos operadores é definido por métodos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuário.
'''

class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_area(self):
        return self.x * self.y
    
    #~~~~~~~~~~ADIÇÃO~~~~~~~~~~~~~~~~
    def __add__(self, other): 
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)
    
    #~~~~~~~~MAIOR QUE~~~~~~~~~~~~~~
    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
    
    #~~~~~~~~MENOR QUE~~~~~~~~~~~~~~
    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
    
    #~~~~~~~~~~IGUALDADE~~~~~~~~~~~~~~~
    def __eq__(self, other):
        if self.x == other.x and self.y and other.y:
            return True
        else:
            return False

    #~~~~~~~~~~Mudando a saída do print~~~~~~~~~~~~
    def __repr__(self):
        return f"<Class 'Retangulo({self.x}, {self.y})'>"
    
    

r1 = Retangulo(10, 20)
r2 = Retangulo(10, 10)
r3 = r1 +r2

print(r1 == r3)
