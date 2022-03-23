'''
Estruturas de repetição loop for
loop > e uma estrutra de repetição
for > uma dessa estruturas
Python
for intem in interavel
    //ececução do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis
Exemplos de iteraveis:
String
    nome = "Geek University'
lista
    lista = [1, 3, 5, 7, 9]
Range
    numeros = range(1, 10)

# Exemplo de for 1 (string)
for letra in nome:
    print(letra)
# Exemplo de for 2 (lista)
for numero in lista:
    print(numero)
# Exemplo de for 3 (range)

range(valor_inicial, valor_final)

for numero in range(1, 11):
    print(numero)
for indicie, letra in enumerate(nome):
    print(nome[indice])
for indice, letra in enumerate(nome):
    print(letra)
for _, letra in enumerate(nome)
    print(letra)
Obs Quando nao precisamos de um valor, podemos descatar utilizando _             

nome = 'Geek Universty'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

for valor in enumerate(nome):
    print(valor)
qtd = int(input('Quantos vezes de rodar: '))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome =  'Geek Universty'
for letra in nome:
    print(letra, end='')
Tabela de Emojis Inicode: https://apps.timwhitlock.info/emoji/tables/unicode
'''
# original:U+1F60D
# modificado: U000F60D
emoji = 'U000F60D'

for num in range(1, 11):
    print('\U000F60D' * num)




