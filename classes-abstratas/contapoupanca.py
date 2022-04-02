from conta import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente.')
            return
        
        if not isinstance(valor, (int, float)):
            raise ValueError('O seu saldo precisa ser um valor númerico.')

        self.saldo -= valor
        self.detalhes()
