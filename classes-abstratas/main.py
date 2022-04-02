from contapoupanca import ContaPoupanca
from concacorrente import ContaCorrente

cp = ContaPoupanca(111, 222, 0)
cp.depositar(10)
cp.sacar(3)
cp.sacar(7)
cp.sacar(1)

print()
print('~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~')
print()

cc = ContaCorrente(11, 22, 0, 500)
cc.depositar(100)
cc.sacar(500)

