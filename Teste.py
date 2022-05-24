Cardapio = [['Cachorro_Quente',100, 1.20],['Bauru-simples',101,1.30],['Bauru-ovo',102,1.50],['Hamburguer',103,1.20],['Cheeseburguer',104,1.70],['Refrigerante',106,1.00],['Suco',107,1.50]]
Pedido = []
Quantidade = 0
Preco = 0
codigos = [c[1] for c in Cardapio]
Descricao = [c[0] for c in Cardapio]
codigo = int(input('Digite o codigo do produto, ou 0 para sair: '))
while codigo != 0:

    if codigo in codigos:
        Quantidade = int(input('Digite a quantidade: '))
        for c in Cardapio:
            if c[1] == codigo:
                Preco = Quantidade * c[2]
                Pedido.append([c[0],Preco])
                print(f'{c[0]} adicionado ao pedido\n')
                print(f'{Pedido}\n')

    else:
        print('Codigo invalido')
    codigo = int(input(' Digite o codigo do produto, ou 0 para sair: '))
Pedido_final = [c[1] for c in Pedido]
Total = sum(Pedido_final)
print(f'{Pedido}')
print(f'O valor total do seu pedido  e: {Total}')


