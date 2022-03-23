'''
Listas sao mutaveis
listas em python funcionam como vetores ou matrizes, com diferença de ser dinamicos e tambem qualquer tipico de dados.
Obs

Linguagem c/Java: Arrays
    Possuem tamanho o tipo de dado fixo
    ou seja nesta linguagen se vc criar um array do tipo int e tamanha 5 sera sempre do tipo inteiro e podera ter
    sempre no maximo 5
ja em Python:
Dinamico: Nao possui tamanho fixo: ou seja podemos criar a lista e  simplesmente e adicionando elementos
Qualquer tipo de dado: Não possuem tipo de dados fixos, podemos colocar qualquer tipo de dados
As listas em python sao representadas em []

# Podemos facilmente checar se determinado valor esta contido na lista

num = input('digite um numero: ')
if int(num) in lista4:
    print(f'Encontrei o numero {num} ')
else:
    print(f'Nao encontrei o numero {num} ')

#Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)
# Podemos facilmente conta o numero de ocorrencia de um valor
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas
Para adicionar elementos em listas, utilizamos a função append
Obs com append nos so conseguimos adiconar um elemento por vez

print(lista1)
lista1.append(42)
print(lista1)
lista1.append([8, 3, 1]) # Coloca cada elemento de lista unico
print(lista1)
lista1.extend([10, 15, 17]) # Coloca cada elemento na lista
print(lista1)

if [8, 3, 3] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')
forma 1 : lista1.reverse()
forma2 : print(lista1[::-1])

# Podemos contar quantos elementos existem dentro da lista
print(len(lista5))
# Podemos remover facilmente o ultimo elemento de uma lista
lista5.pop()
# Podemos remover pelo indice tb
lista5.pop(2) ira remover o elemento do indice na posição 2
# Podemos limpara tb a nossa lista
lista5.clear()
# Podemos repetir elementos em uma lista
nova = [1, 2, 3,]
nova = nova * 3
#Abaixo estamos falando em colocar espaço em cada elemento
Converter uma lista em uma string
curso = ' '.join(lista6)
# Abaixo estamos falando em colocar $ em cada elemento
curso = '$'.joint(lista6
# Iterando sobre lista
# Exemplo1 Utilizando for

for elemento in lista1:
    print(elemento)
# Exemplo 2 -  utilizando While
carrinho = []
produto = ''
while produto != 'sair':
    print("Adicionar um produto na lista ou digite: 'sair' ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)
# Fazemos acessos aos elementos de forma indexada
cores = ['verde', 'amarelo', 'azul' 'verde']
print(cores[1])
print(cores[3])
# Fazemos acesso aos elementos de forma indexada iversa
print(cores[-1])

for cor in cores:
    print(cor)
indice = a
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
# Gerar indice em um for
for incice, cor in enumerate(cores):
    print(indice, cor)
# listas aceitam valores repetidas

# Outros metodos nao tao importante mas tb uteis
# Encontrar o indice de um elemento na lisa
numeros = [5, 6, 7, 8, 9, 10, 5]
print((numeros.index(6)))
# Obs caso nao tenha esse elemento na lista sera apresentado erro
# Retorna o indice do primeiro elemento encotrado
# Podemos fazer uma busca dentro de uma range,  ou seja, qual indice começa a buscar
print(numeros.index(5, 1))

# Revisao de slicing
# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slice de lista com parametro 'incio'
lista = [1, 2, 3, 4]
print(lista[1:]) inicia no indice 1 e pegando todos restante

# Trabalhando com slice de lista com parametro 'fim'
print(lista[:2])
print(list1[:3])

# Trabalhando com slice de lista com parametro 'passo'
print(lista[::2])
print(lista[1::3])

# Invertando valores em uma lista

nome = ['Geek', 'Universty ']
nome[0], nome[1] = nome[1], nome[0]
print(nome)
nome = ['Geek', 'Universty ']
nome.reverse()
print(nome)

# Soma, Valor Maximo, valor minimo, tamanho
se os valores forem inteiro ou real
lista[1, 2, 3, 4, 5, 6]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))
# Transformar uma lista em tupla
tupla = tuple(lista)
#Desempacotamento de listas
lista = [1, 2, 3]
num1, num2, num3 = lista
Obs se tivermos mais elementos para desempacotar do que variavel teremos ValueError

# Copia de lista
copiando um lista para outra(shallow copy e Deep copy)
print(lista1)
nova = lista1.copy()
print(nova)
nova.append(4)
print(lista1)
print(nova)
# Veja que ao utilizarmos lista1.copy obtemos os dados da lista1 copiada para uma nova lista
# E ficaram independentes ou seja modificando uma lista nao afeta a outra
# Em Python nos chamos de Deep copy( copia profunda
# Forma 2 de copia
Veja que utilizamos a copia via de atribuição e copiamos os dados mas se fizer um modificação
em qualquer uma a outra e modificada
Isso em Pyhton e chamdo de Shallow copy

nova = lista1

'''
type([])
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = ['S', 'a', 'n', 'd', 'r', 'o']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')
lista6 = ['Programaçao', 'em', 'Python', 'Essencial']
lista7 = [1, 2.36, 'sandro', True]
cores = ['verde', 'amarelo', 'azul', 'branco']

