'''
1 Digite dois numeros e iprima o maior numero
num1 = input('Digite o numero1:')
num2 = input('Digite o numero2:')
if num1 > num2:
    print(num1)
else:
    print(num2)

----------------------------------------------
2 Digite um numero se ele for positivo mostre a raiz quadrada senao mostre numero invalido

num = input('Digite um numero: ')
if num >= "0":
    print(float(num) ** (1/2))
else:
    print('Esse numero e invalido ')

----------------------------------------------
3 Digite um numero real - positivo raiz quadrada - negativo o quadrado

num = input('Digite um numero: ')
if num >= "0":
    print(float(num) ** (1/2))
else:
    print(float(num) ** 2 )
----------------------------------------------
4 Digite um numero se for positvo mostre a raiz e o quadrado desse numero

num = input('Digite um numero: ')
if num >= "0":
    print(float(num) ** (1/2))
    print(float(num) ** 2)

5 Digite um numero real e verifique se ele e impar ou par

num = int(input("Digite um numero inteiro: "))
restD = (num) % 2
if restD == 0:
    print('Esse numero é par')
else:
    print('Esse numero e impar')
------------------------------------------------
6 Digite dois numero e mostre o maior numero e a diferença entre eles

num1 = input('Digite num1:')
num2 = input('Digite num2:')
if num1 > num2:
    print(num1)
    print(int(num1) - int(num2))

else:
    print("O numero2 e o maior numero:", num2)
    print(int(num2) - int(num1))
----------------------------------------------
7 Digite dois numeros imprima o maior e a diferença, se for iguais escreva numeros iguais

num1 = input('Digite num1:')
num2 = input('Digite num2:')
if num1 > num2:
    print(num1)
    print(int(num1) - int(num2))
elif num1 < num2:
    print(num2)
    print(int(num2) - int(num1))

elif num1 == num2:
    print('Numero iguais')
---------------------------------------

8 Digite se duas notas sao validas entre 0 e 10 e imprima

nota1 = input('Digite uma nota1: ')
nota2 = input('Digite uma nota2: ')
if 0 < int(nota1) < 10 and 0 < int(nota2) < 10:
    print('notas validas:')

else:
    print('nota invalida')

--------------------------------------------------
9 Digite um salario e o valor da parcela do emprestimo se for maior que 20% nao concedido
salarioT = input('Digite o seu salario: ')
valorPrestacao = input('Digite valor da parcela: ')
if float(valorPrestacao) > (float(salarioT) * 0.20):
    print('Emprestimo nao concedido')

else:
    print('Emprestimo concedido: ')
-------------------------------------------------
10 Digite a altura e o sexo e imprima conforme a tabela abaixo
altura = input("Digite a sua altura: ")
sexo = input("Digite seu sexo: Masculino(m) feminino(f): ")
if sexo == 'm':
    print(72.7 * float(altura)-58 )
elif sexo == 'f':
    print(62.1 * float(altura)-44.7)

----------------------------------------------------------
11 Digite um numero e soma os algoritmos desse numero
num = input('Digite um numero: ')
soma = 0
if float(num) > 0:
    for n in num:
        soma = soma + int(n)
    print(f'A soma dos Algoritimos de {num} é {soma}')
else:
    print(f'Numero invalido:')
-------------------------------------------------------
12 Digite um numero se for positivo calcule o logaritimo desse numero, negativo numero invalido

import math

num = int(input('Digite um numero: '))
resultado = math.log(num)

if float(num) < 0:
    print(f'Numero invalido')
else:
    print(f'O logaritimo de {num} é {resultado}')

-----------------------------------------------------
13 Digite 3 notas onde a 1 e 2 peso 1 e 3 nota peso 2 calucule media poderada
nota1 = input("Digite a nota1: ")
nota2 = input("Digite a nota2: ")
nota3 = input("Digite a nota3: ")
mediaPonderada = ((float(nota1)*1) + (float(nota2)*1) + (float(nota3)*2))/3
if mediaPonderada >= 60:
    print(f'A nota do aluno foi: {mediaPonderada} - Aprovado')
else:
    print(f'A nota do aluno foi: {mediaPonderada} - Reprovado')

-----------------------------------------------------
14 Digite 3 notas com pesos diferentes e imprima se esta aprovado, recuperação ou reprovado

notaT = input("Digite a notaT: ")

notaSemestre = input("Digite a notaSemestre: ")

notaFinal = input("Digite a notaFinal: ")

mediaPonderada = ((float(notaT)*2) + (float(notaSemestre)*3) + (float(notaFinal)*2))/3

if mediaPonderada >= 5:
    print(f'A nota do aluno foi: {mediaPonderada} - Aprovado ')

elif 2.9 < mediaPonderada < 5:
    print(f'Sua nota é {mediaPonderada} - Recuperação ')

elif mediaPonderada < 3:
    print(f'Sua nota é {mediaPonderada} - Reprovado ')

-----------------------------------------------------

15 Digite um numero e o correspondente na semana

numero = int(input('Digite um numero: '))
if numero == 1:
    print(f'O dia da semana é Domingo ')
elif numero == 2:
    print(f'O dia da semana é Segunda ')

elif numero == 3:
    print(f'O dia da semana é Terça ')

elif numero == 4:
    print(f'O dia da semana é Quarta ')

elif numero == 5:
    print(f'O dia da semana é Quinta ')

elif numero == 6:
    print(f'O dia da semana é Sexta ')

elif numero == 7:
    print(f'O dia da semana é Sabado ')

----------------------------------------------------

15 Digite um numero e descubra o equivalente do mes

numero = int(input('Digite um numero: '))
if numero == 1:
    print(f'O dia do mes e Janeiro ')
elif numero == 2:
    print(f'O dia do mes e Fevereiro ')

elif numero == 3:
    print(f'O dia do mes e Marco ')

elif numero == 4:
    print(f'O dia do mes e Abril')

elif numero == 5:
    print(f'O dia do mes e Maio ')

elif numero == 6:
    print(f'O dia do mes e Junho ')

elif numero == 7:
    print(f'O dia do mes e Julho ')

elif numero == 8:
    print(f'O dia do mes e Agosto ')

elif numero == 9:
    print(f'O dia do mes e Setembro ')

elif numero == 10:
    print(f'O dia do mes e Outubro ')

elif numero == 11:
    print(f'O dia do mes e novembro ')

elif numero == 12:
    print(f'O dia do mes e Dezembro ')
Forma 2
type([])
lista = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
num = input('digte um numero referente ao mes:  ')
print(f'O mês referente a esse numero é {lista[int(num) -1]} ')



------------------------------------------------
17 Calcule a area do trapezio

baseMaior = input('Digite o valor da base maior: ')
baseMenor = input('Digite o valor da base menor: ')
altura = input("Digite a altura: ")
area = (float(baseMaior) + float(baseMenor)) * float(altura) /2
print(f"A area do trapezio e {area}")

------------------------------------------------

18 mostre um operador e o que usuario digitar faca a operação

operadores = input('Digite qual e a operação: (+) (-) (*) (/) : ')
num1 = input('Digite o num1: ')
num2 = input('Digite o num2: ')

if operadores == '+':
    soma = float(num1) + float(num2)
    print(f'Resutado = {soma}')
elif operadores == '-':
    soma = float(num1) - float(num2)
    print(f'Resutado = {soma}')

elif operadores == '*':
    soma = float(num1) * float(num2)
    print(f'Resutado = {soma}')

elif operadores == '/':
    soma = float(num1) / float(num2)
    print(f'Resutado = {soma}')
-----------------------------------------------
19 faça um programa que leia se o numero e divido por 3 e 5

num = int(input('Digite um numero inteiro: '))
resultado1 = int(num) % 3 == 0
resultado2 = int(num) % 5 == 0
if resultado1 == True and resultado2 == False:
    print('E divisivel por 3 e não e divisivel pro 5 ')

elif resultado1 == False and resultado2 == True:
    print('E divisivel por 5 e não e divisivel pro 3 ')

21

print('Escolha as opções abaixo: ')
print((f"(1) para soma de 2 numeros" ))
print((f'(2) para diferença de dois numeros: '))
print((f'(3) para produto entre numeros'))
print((f'(4) para divisao de 2 numeos'))

opcao = input(f'Digite a sua opacao: ')
num1 = int(input('Digite o numero 1: '))
num2 = int(input('Digite o numero 2: '))

if opcao == '1':
    resultado1 = float(num1) + float(num2)
    print(resultado1)
elif opcao == '2':
    if int(num1) > int(num2):
        resultado2 = int(num1) - int(num2)
        print(resultado2)
    else:
        resultado21 = int(num2) - int(num1)
        print(resultado21)

elif opcao == '3':
    resultado3 = int(num1) * int(num2)
    print(resultado3)

elif opcao == '4':
    resultado4 = int(num1) / int(num2)
    print(resultado4)
    print(int(num1) % int(num2))
-----------------------------------------------
22

idade = input('Digite sua idade: ')
tempo = input("Digite tempo trabalhado: ")
if int(idade) >= 65:
    print('Voce esta aposentado')

elif int(tempo) >= 30:
    print("Voce esta aposentado")
elif int(idade) >= 60 and int(tempo) >= 25:
    print('Voce esta aposentado')

else:
    print('Voce nao esta aposentado ')

23
ano = input('Digite um ano: ')

if int(ano) % 4 == 0 or int(ano) % 400 == 0 and int(ano) % 100 != 0 :
    print(f"Esse ano de {ano} é Bissexto: ")
else:
    print(f'Esse ano {ano} nao e Bissexto ')


24 Digite o estado e calcule o valor do produto conforme o imposto
produto = input('Digite o valor do produto: ')
estado = input('Digite o seu estado: ')

mg = 1.07
sp = 1.12
rj = 1.15
ms = 1.08

if estado == 'mg':
    print(f'O valor do produto é:R$', float(produto) * float(mg))

elif estado == 'sp':
    print(f'O valor do produto é:R$', float(produto) * float(sp))

elif estado == 'rj':
    print(f'O valor do produto é:R$', float(produto) * float(rj))

elif estado == 'ms':
    print(f'O valor do produto é:R$', float(produto) * float(ms))
-----------------------------------------------
27
km = input('Digite quantos km rodados: ')
litros = input('Digite quantos litros gastos: ')
resultado = float(km) / float(litros)
if resultado < 8:
    print('Venda o carro:')
elif 8 < resultado < 12:
    print('Economico')

elif resultado > 12:
    print('Super Economico')

---------------------------------------------
27
idade = input('Digite a data do nadador: ')
if 5<= int(idade) <=7:
    print('Categoria infantil A')

elif 8<= int(idade) <= 10:
    print('Categoria infantil B')

elif 11<= int(idade) <= 13:
    print('Categoria Junior A')

elif 14<= int(idade) <= 17:
    print('Categoria junior B')

elif int(idade) >= 18:
    print('Categoria Senior ')
-------------------------------------------
28

Calcule as medias
x = input('Digite o valor de x: ')
y = input('Digite o valor de y: ')
z = input('Digite o valor de z: ')

geometria = (int(x) * int(y) * int(z)) * (1/3)
ponderada = ((int(x) + 2) * (int(y) + 3) * int(z)) / 6
harmonica = 1 / (1/int(x)) + (1/int(y)) + (1/int(z))
aritimetica = (int(x) + int(y) + int(z))/3

print(f'a media Gemetrica è {geometria}')
print(f'a media Ponderada è {ponderada}')
print(f'a media Harmonica è {harmonica}')
print(f'a media Aritimetica è {aritimetica}')

----------------------------------------------------

30
num1 = input('Digite o primeiro numero:')
num2 = input('Digite o segundo numero:')
num3 = input('Digite o terceiro numero:')
print(sorted((int(num1), int(num2), int(num3))))
31

altura = input('Digite sua altura: ')

peso = input('Digite seu peso: ')

if float(altura) < 1.2 and float(peso) < 60:
    print('Sua classificação e A')

elif float(altura) < 1.2 and 60 <= float(peso) <= 90:
    print('Sua classificação e D')

elif float(altura) < 1.2 and  float(peso) > 90:
    print('Sua classificação e G')

elif 1.2 <= float(altura) <= 1.7 and  float(peso) < 60:
    print('Sua classificação e B')

elif 1.2 <= float(altura) <= 1.7  and 60 <= float(peso) <= 90:
    print('Sua classificação e E')

elif 1.2 <= float(altura) <= 1.7 and  float(peso) > 90:
    print('Sua classificação e H ')

elif  float(altura) > 1.7 and  float(peso) <= 60:
    print('Sua classificação e C')

elif  float(altura) > 1.7 and  60 <= float(peso) <= 90:
    print('Sua classificação e F')

elif  float(altura) > 1.7 and  float(peso) > 90:
    print('Sua classificação e I')

--------------------------------------------------

32
cachorroQuente = 1.2
bauruSimples = 1.3
bauruOvo = 1.5
hamburguer = 1.2
chesseBurguer = 1.7
suco = 2.2
refrigerante = 1
sair = True
preco1 = 0
preco2 = 0
preco3 = 0
preco4 = 0
preco5 = 0
preco6 = 0
preco7 = 0
while sair != 'n':
    codigo = input('Digite o codigo do produto: ')
    quantidade = int(input('Digite a quantidade: '))
    sair = input('tem mais produtos: ? ')
    if codigo == '100':
        preco1 = int(quantidade) * float(cachorroQuente)
        print(preco1)
    elif codigo == '101':
        preco2 = int(quantidade) * float(bauruSimples)
        print(preco2)
    elif codigo == '102':
        preco3 = int(quantidade) * float(bauruOvo)
        print(preco3)
    elif codigo == '103':
        preco4 = int(quantidade) * float(hamburguer)
        print(preco4)
    elif codigo == '104':
        preco5 = int(quantidade) * float(chesseBurguer)
        print(preco5)
    elif codigo == '105':
        preco6 = int(quantidade) * float(suco)
        print(preco6)
    elif codigo == '106':
        preco7 = int(quantidade) * float(refrigerante)
        print(preco7)

valorT = float(preco1) + float(preco2) + float(preco3) + float(preco4) + float(preco5) + float(preco6) + float(preco7)
print(f'O valor total do pedido é : {valorT}')

------------------------------------------------------------
33

valorP = input('Digite o valor do produto: ')
valorPn = 0

if float(valorP) < 50 :
    valorPn = int(valorP) * 1.05
    print(f'O novo valor do produto é: {valorPn} ')

elif 50 <= int(valorP) <= 100 :
    valorPn = int(valorP) * 1.10
    print(f'O novo valor do produto é: {valorPn}')

elif int(valorP) > 100 :
    valorPn = int(valorP) * 1.15
    print(f'O novo valor do produto é: {valorPn}')

if valorPn <= 80 :
    print('Barato')

elif 80 <= int(valorPn) <= 120 :
    print('Normal')

elif 120 < int(valorPn) <= 200 :
    print('Caro')

elif int(valorPn) > 200 :
    print('Muito Caro')

------------------------------------------------
34

nota = input('Digite sua nota: ')
faltas = input('Digite suas faltas: ')

if float(faltas) <= 20 and 9 <= float(nota) <= 10:
    print('Seu conceito e A ')


elif float(faltas) <= 20 and 7.5 <= float(nota) <= 8.9:
    print('Seu conceito e B ')

elif float(faltas) <= 20 and 5 <= float(nota) <= 7.4:
    print('Seu conceito e C ')

elif float(faltas) <=20 and 4 <= float(nota) <= 4.9:
    print('Seu conceito e D')

elif float(faltas) <=20 and  0 <= float(nota) <= 3.9:
    print('Seu conceito e E')

elif float(faltas) > 20 and 9 <= float(nota) <= 10:
    print('Seu conceito e B ')

elif float(faltas) > 20 and 7.5 <= float(nota) <= 8.9:
    print('Seu conceito e C ')

elif float(faltas) > 20 and 5 <= float(nota) <= 7.4:
    print('Seu conceito e D ')

elif float(faltas) > 20 and 4 <= float(nota) <= 4.9:
    print('Seu conceito e E')

elif float(faltas)  > 20 and  0 <= float(nota) <= 3.9:
    print('Seu conceito e E')

--------------------------------------------------------

35 Digite uma data e verifique se a data e valida ou nao

data = input('Digite a data: dd/mm/yyyy: ')
dia, mes, ano = data.split('/')
dia = int(dia)
mes = int(mes)
ano = int(ano)
valide = False
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if int(dia) <= 31:
        valide = True
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if int(dia) <= 30:
        valide = True

elif mes == 2:
    if int(ano) % 400 == 0 and int(ano) % 100 != 0 or int(ano) % 4 == 0 :
        if int(dia) <= 29:
            valide = True
    else:
        if int(dia) <= 28:
            valide = True

if valide == True:
    print('Data valida')
else:
    print('Data invalida')


36
vendaMensal = input('Digite o valor da venda mensal: ')

if float(vendaMensal) >= 100000 :
    comissao = 700 + (float(vendaMensal) * 0.16)

elif 80000 <= float(vendaMensal) < 100000:
    comissao = 650 + (float(vendaMensal) * 0.14)

elif 60000 <= float(vendaMensal) < 80000:
    comissao = 600 + (float(vendaMensal) * 0.14)

elif 40000 <= float(vendaMensal) < 60000:
    comissao = 550 + (float(vendaMensal) * 0.14)

elif 20000 <= float(vendaMensal) < 40000:
    comissao = 500 + (float(vendaMensal) * 0.14)

elif float(vendaMensal) < 20000:
    comissao = 400 + (float(vendaMensal) * 0.14)

print(f'Sua comisao é: {comissao}')

----------------------------------------------------
37

horaChegada = input("Digite a hora chegada: ")
horaC, minutosC, = horaChegada.split(':')
horaC = int(horaC)
minutosC = int(minutosC)
horaSaida = input('Digite a hora de saida: ')
horaS, minutosS, = horaSaida.split(':')
horaS = int(horaS)
minutosS = int(minutosS)
tempoH = int(horaS) - int(horaC)
tempoM = int(minutosS) - int(minutosC)

if 0 < int(tempoM) <= 60:
    tempoH = tempoH + 1

elif 60 < int(tempoM) < 120:
    tempoH = int(tempoH) + 2

tempoT = int(tempoH)
print(f'O seu tempo total é: {tempoT} Hora')
valorPagar = 0

if 1 <= int(tempoT) <= 2:
    valorPagar = int(tempoT) * 1

elif 2 < int(tempoT) <= 4:
    valorPagar = int(tempoT) * 1.4

elif int(tempoT) > 4:
    valorPagar = int(tempoT) * 2

print(f'O valor a ser pagor é: R$ {valorPagar} ')

--------------------------------------------------------------

39

salarioAtual = int(input('Digite o salario atual: '))
tempoServico = float(input('Digite Quantos anos de serviço: '))

bonus = 0
if (salarioAtual) <= 500 and  int(tempoServico) < 1:
    bonus = 0
    salarioFinal = (float(salarioAtual) * 0.25) + int(bonus) + float(salarioAtual)
    print(f'O seu salario final é {salarioFinal}')
elif int(salarioAtual) <= 500 and  1 <= int(tempoServico) <= 3:
    bonus = 100
    salarioFinal = (float(salarioAtual) * 0.25) + int(bonus) + float(salarioAtual)
    print(f'O seu salario final é {salarioFinal}')
elif float(salarioAtual) <= 500 and 4 <= int(tempoServico) <= 6:
    bonus = 200
    salarioFinal = (float(salarioAtual) * 0.25) + int(bonus) + float(salarioAtual)
    print(f'O seu salario final é {salarioFinal}')
elif float(salarioAtual) <= 500 and 7 <= int(tempoServico) <= 10:
    bonus = 300
    salarioFinal = (float(salarioAtual) * 0.25) + int(bonus) + float(salarioAtual)
    print(f'O seu salario final é {salarioFinal}')
elif float(salarioAtual) <= 500 and int(tempoServico) > 10:
    bonus = 500
    salarioFinal = (float(salarioAtual) ) + int(bonus)
    print(f'O seu salario final é {salarioFinal}')

if  500 < (salarioAtual) <= 1000 and  int(tempoServico) < 1:
    bonus = 0
    salarioFinal = (float(salarioAtual) * 0.20) + int(bonus) + float(salarioAtual)
    print(f'O seu salario final é {salarioFinal}')
elif 500 < (salarioAtual) <= 1000 and  1 <= int(tempoServico) <= 3:
    bonus = 100
    salarioFinal = (float(salarioAtual) * 0.20) + int(bonus) + float(salarioAtual)
    print(f'O seu salario final é {salarioFinal}')
elif 500 < (salarioAtual) <= 1000 and 4 <= int(tempoServico) <= 6:
    bonus = 200
    salarioFinal = (float(salarioAtual) * 0.20) + int(bonus) + float(salarioAtual)
    print(f'O seu salario final é {salarioFinal}')
elif 500 < (salarioAtual) <= 1000 and 7 <= int(tempoServico) <= 10:
    bonus = 300
    salarioFinal = (float(salarioAtual) * 0.20) + int(bonus) + float(salarioAtual)
    print(f'O seu salario final é {salarioFinal}')
elif 500 < (salarioAtual) <= 1000 and int(tempoServico) > 10:
    bonus = 500
    salarioFinal = (float(salarioAtual) ) + int(bonus)
    print(f'O seu salario final é {salarioFinal}')

if  1000 < (salarioAtual) <= 1500 and  int(tempoServico) < 1:
    bonus = 0
    salarioFinal = (float(salarioAtual) * 0.15) + int(bonus) + float(salarioAtual)
    print(f'O seu salario final é {salarioFinal}')
elif 1000 < (salarioAtual) <= 1500 and  1 <= int(tempoServico) <= 3:
    bonus = 100
    salarioFinal = (float(salarioAtual) * 0.15) + int(bonus) + float(salarioAtual)
    print(f'O seu salario final é {salarioFinal}')
elif 1000 < (salarioAtual) <= 1500 and 4 <= int(tempoServico) <= 6:
    bonus = 200
    salarioFinal = (float(salarioAtual) * 0.15) + int(bonus) + float(salarioAtual)
    print(f'O seu salario final é {salarioFinal}')
elif 1000 < (salarioAtual) <= 1500 and 7 <= int(tempoServico) <= 10:
    bonus = 300
    salarioFinal = (float(salarioAtual) * 0.15) + int(bonus) + float(salarioAtual)
    print(f'O seu salario final é {salarioFinal}')
elif 1000 < (salarioAtual) <= 1500 and int(tempoServico) > 10:
    bonus = 500
    salarioFinal = (float(salarioAtual) ) + int(bonus)
    print(f'O seu salario final é {salarioFinal}')

-------------------------------------------------------------------------------------------
40



custoFabrica = float(input('Digite o custo da fabrica: '))

if custoFabrica <= 12000:
    custoDistribuidor = 0.05
    impostos = 0
    comissao = (custoFabrica * custoDistribuidor)
    valorImpostos = (custoFabrica * impostos)
    valorFinal = custoFabrica + comissao + valorImpostos
    print(f'O valor da comissao é: {comissao} e o valor dos impostos é {valorImpostos} ')
    print(f'O valor final do carro é: {valorFinal}')

elif 12000 <= custoFabrica <= 25000:
    custoDistribuidor = 0.10
    impostos = 0.15
    comissao = (custoFabrica * custoDistribuidor)
    valorImpostos = (custoFabrica * impostos)
    valorFinal = custoFabrica + comissao + valorImpostos
    print(f'O valor da comissao é: {comissao} e o valor dos impostos é {valorImpostos} ')
    print(f'O valor final do carro é: {valorFinal}')

elif custoFabrica > 25000:
    custoDistribuidor = 0.15
    impostos = 0.20
    comissao = (custoFabrica * custoDistribuidor)
    valorImpostos = (custoFabrica * impostos)
    valorFinal = custoFabrica + comissao + valorImpostos
    print(f'O valor da comissao é: {comissao} e o valor dos impostos é {valorImpostos} ')
    print(f'O valor final do carro é: {valorFinal}')

---------------------------------------------------------------------------
41
'''

altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

imc = (peso) / (altura) ** 2

if float(imc) < 18.5:
    print(f'Voce esta Abaixo do peso: {imc}')

elif 18.6 <= (imc) <= 24.9:
    print(f'Voce esta Saudavel: {imc}')

elif 25 <= (imc) <= 29.9:
    print(f'Voce esta com Peso em excesso: {imc}')

elif 30 <= (imc) <= 34.9:
    print(f'Voce esta Obesidade Grau I: {imc}')

elif 35 <= (imc) <= 39.9:
    print(f'Voce esta com Obesidade Grau II: {imc}')

elif (imc) >= 40:
    print(f'Voce esta com Obesidade Grau III(morbida): {imc}')
