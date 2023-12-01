class Main:
    pass

print("teste")

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("Joao", "119988-5647")
conta = Conta(c1.get_nome(), 6556,0)

conta.deposita(5000)
conta.saque(100)
conta.extrato()