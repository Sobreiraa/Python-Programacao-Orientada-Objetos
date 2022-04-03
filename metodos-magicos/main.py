'''
https://rszalski.github.io/magicmethods/
'''

class A:
    def __init__(self):
        print('Eu sou o INIT.')
    
    # Criando apenas uma instância
    '''def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)

        return cls._jaexiste
    '''

    # Faz com que a classe se comporte como uma função
    '''
    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
    '''

    # É chamado toda vez que tentamos utilizar a classe como string
    '''
    def __str__(self):
        return "<class 'a'>"
    '''

a = A()
print(a)
'''a(1,2,3,4,5, nome='Matheus')'''