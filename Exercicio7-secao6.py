'''
Exercicio 1

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = 1
qtd = 0
for n in numero:
    if n % 3 == 0:
        print(n)
        n = n + 1
        qtd += 1
    elif qtd == 5:
        break
-----------------------------------------------------------
2
numero = range(0, 100)
for n in numero:
    print(n + 1 )

n = 1
numeros = range(0, 100)
while int(n) <= 100:
    print(n)
    n  = n + 1

-----------------------------------------------------------
3

numeros = range(0, 10)
n = 10
while int(n) >= 0:
    print(n)
    n = n - 1

print('Fim')

--------------------------------------------------------
4

n = 0
while n <= 100000:
    print(n)
    n = n + 1000

---------------------------------------------------------
5

qtd = 10
soma = 0
for n in range(1, qtd+1):
    num = input(f'Digite o numero {n}/{qtd}: ')
    soma = soma + int(num)
print(soma)
-------------------------------------------------------

6

numeros = range(1, 11)
n = 0
soma = 0
for n in numeros:
    soma = int(soma) + n
    print(n)
print(soma)
media = soma / 10
print(f'A media dos numeros é: {media} ')

-------------------------------------------------------

7

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in numeros:
    numeros.sort()
    print(len(numeros))
    print(f' O menor numero é: {numeros[0]}, e o maior numero é:  {numeros[9]}')
    break

--------------------------------------------------------
9
numeros = range(1, 10, 2)
n = 0
for n in numeros:
    print(n)
    n = n + 1
----------------------------------------------------------
10

numeros = range(0, 52, 2)
n = 0
soma = 0
for n in numeros:
    print(n)
    n = n + 1
print(sum(numeros))
----------------------------------------------------------

11
numero = int(input("Digite um numero inteiro: "))
numeros = range(1, numero+1)
n = 0
for n in numeros:
    print(n)
    n = n + 1
--------------------------------------------------------

12

numero = int(input("Digite um numero inteiro: "))
numeros = range(1, numero+2)
n = numero
for n in numeros:
    n = n - 1
    print(n)

--------------------------------------------------
13
numero = int(input("Digite um numero inteiro: "))
numeros = range(1, numero, 2)
n = 0
for n in numeros:
    n = n + 1
    print(n)

---------------------------------------------
14
numero = int(input("Digite um numero inteiro: "))
numeros = range(1, numero+2, 2)
n = numero
for n in numeros:
    n = n - 1
    print(n)

------------------------------------------------


A = [1,2,3,4,5,6]
A.append(1)
A.append(0)
A.append(5)
A.append(-2)
A.append(-5)
A.append(7)

soma = A[0]+A[1]+A[5]
print(soma)
A[4]= 100
print(A)
for n in A:
    print(n)


import math


a = list(range(1,11))
print(a)
b = []
for n in a:
    n = (n ** 2)
    b.append(n)
print(b)

pares = 0
lista = list(range(1,11))
for n in lista:
    if n % 2 == 0:
        pares = pares + 1
        print(n)
print(pares)
'''
lista = []
while len(lista) <= 10:
    valor = int(input("Digite um numero: "))
    lista.append(valor)
print(max(lista))
print(min(lista))





    

