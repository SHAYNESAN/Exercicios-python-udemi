class ContaCorrente :

    contador = 500
    contador_id = 1
    
    def __init__(self,nome_cliente,saldo, limite):
        self.numero_conta = ContaCorrente.contador
        self.nome_cliente = nome_cliente
        self.saldo = saldo
        self.limite = limite
        self.limite_total = saldo + limite
        ContaCorrente.contador += 1
        ContaCorrente.contador_id += 1

    def sacar_dinheiro(self,valor):
        self.valor = valor
        if valor > 0 and valor <= self.limite_total:
            self.saldo -= valor
            self.limite_total -= valor 

    def Depositar(self,valor):
        self.valor = valor
        if valor > 0:
            self.saldo += valor
            self.limite_total += valor


cc1 = ContaCorrente('Sandro',200,1500)
cc2 = ContaCorrente('Simone',300,2000)

cc1.sacar_dinheiro(50)
cc2.Depositar(450)


print(cc1.numero_conta)
print(cc2.numero_conta)
print(cc1.nome_cliente)
print(cc2.nome_cliente)
print(cc1.saldo)
print(cc2.saldo)
print(cc1.limite)
print(cc2.limite)
print(cc1.limite_total)
print(cc2.limite_total)
print(cc1.__dict__)
print(cc2.__dict__)



