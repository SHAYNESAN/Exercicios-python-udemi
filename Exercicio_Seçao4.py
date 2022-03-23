'''
(1) Leia um numero inteiro e o imprima
numero = int(1)
print(numero)
print(type(numero))
-----------------------------------------------
(2) Leia um numero real e o imprima
numero2 = float(2.5)
print(numero2)
print(type(numero2))
----------------------------------------------
(3) Digite o valor1 o valor2 o valor3 e imprima o resultado inteiro
valor1 = input('Digite valor1:')

valor2 = input('Digite valor2:')

valor3 = input('Digite valor3:')

resultado = int(valor1) + int(valor2) + int(valor3)

print("O Resultado é : " , (resultado))

----------------------------------------------
(4) Leia um valor real e imprima o quadrado desse numero

valor = 3.12
resultado = float(valor) * float(valor)

print("O Quadrado do valor é: ", resultado)
-----------------------------------------------
(5) Leia um numero real e imprima a quinta parte dele

valor1 = 10
operacao = float(valor1) / float(5)
print(operacao)

------------------------------------------------
(6) Conversao de Celsius para Fahrenhiet :

temperaturaC = input("Digite a temperatura em Celsius: ")
temperaturaF = int(temperaturaC)*(9.0/5.0) + (32)
print("A conversão da temperatura em Fahrenhiet é :", temperaturaF)
------------------------------------------------
(7) Conversao de Fahrenhiet para Celsius:

temperaturaF = input("Digite a temperatura em Fahrenheit: ")
temperaturaC = int(5) * (int(temperaturaF) - 32) / int(9)
print("A conversão da temperatura em Celsius é :", temperaturaC)

------------------------------------------------
(8) Conversao de Kelvin para Celsius

temperaturak = input("Digite a temperatura em Kelvin: ")
temperaturaC = float(temperaturak) - float(273.15)
print("A conversão da temperatura em Celsius é :", temperaturaC)

-----------------------------------------------
(9) Converao de Celsius para Kelvin

temperaturaC = input("Digite a temperatura em Celsius: ")
temperaturaK = int(temperaturaC) + float(273.15)
print("A conversão da temperatura em Kelvin é :", temperaturaK)

-----------------------------------------------
(10) Conversao km/h para m/s

kmh = input("Digite a velocidade de km/h: ")
ms = float(kmh) / float(3.6)


------------------------------------------------
(11) (10) Conversao m/s para km/h

ms = input("Digite a sua velocidade em m/s: ")
kmh = int(ms) * float(3.6)
print("A velocidade em km/h é: ", int(kmh),"km/h")

-----------------------------------------------
(12) Conversao Milhas para Km

distanciaM = input("Digita a distancica em milhas: ")
distanciakm = float(distanciaM) * float(1.61)
print("A distancia equivalente em km é:", distanciakm,"km")
------------------------------------------------
(13) Conversao Km para Milhas
distanciaKm = input("Digita a distancica em Quilometros:")
distanciaM = float(distanciaKm)/ float(1.61)
print("A distancia equivalente em Milhas é:", distanciaM,"Ml")

-------------------------------------------------

(14) Conversao Angulos Graus para Angulos Radianos

import math
anguloG = input("Digite o angulo em graus: ")
anguloR = float(anguloG) * math.pi / 180
print("O angulo em radiano equivalente e: ", anguloR)

--------------------------------------------------
(15) Conversao Angulos Radianos para Angulos Graus

import math
anguloR = input("Digite o angulo em radianos: ")
anguloG = float(anguloR) * 180 / math.pi
print("O angulo em Graus equivalente e: ", anguloG)

---------------------------------------------------
(16) Conversap Polegadas para Centimetro

comprimentosP = input("Digite o comprimento em polegadas: ")
comprimentosC = float(comprimentosP) * 2.54
print(comprimentosC)

(17) Conversap Centimetro para Polegada

comprimentoC = input("Digite o comprimento em centimetros: ")
comprimentoP = float(comprimentoC) / 2.54
print(comprimentoP)

---------------------------------------------------
(18) Converter m3 em litros

valorM3 =  input("Digite um volume m3: ")
valaorL = 1000 * float(valorM3)
print("Valor equivalente em litros é: ", valaorL)

--------------------------------------------------
(19) Converter litros em m3

valorL = input("Digite um volume e Litros: ")
valorM3 = int(valorL) / 1000
print("Valor equivalente em metros 3 é: ", valorM3)

--------------------------------------------------
(20) Converter kg para Lb


massakg = input("Digite o valor em kg: ")
massalb = int(massakg) / 0.45
print("O valor de coversao é: ",massalb)
------------------------------------------------
(21) Converter Lb para kg

massaLb = input("Digite o valor em Lb: ")
massakg = int(massaLb) * 0.45
print("O valor de coversao é: ",massakg, "kg")

-----------------------------------------------
(28) Digite 3 valores e a soma do quadrado dos numeros
import math
valor1 = input("Digite um valor1: ")
valor2 = input("Digite um valor2: ")
valor3 = input("Digite um valor3: ")
resultado = int(valor1) ** 2 + int(valor2) ** 2 + int(valor3) ** 2

print(resultado)
----------------------------------------------

(29) Digite o nome aluno de 4 notas e ache a media aritmetica delas

aluno = input("Digite o nome do aluno: ")
nota1 = input("Digite a nota1: ")
nota2 = input("Digite a nota2: ")
nota3 = input("Digite a nota3: ")
nota4 = input("Digite a nota4: ")
resultado = (float(nota1) + float(nota2) + float(nota3) + float(nota4)) / 4

print("A media aritmetica das notas é : ", resultado)

if resultado >= float("6"):
    print("O aluno", aluno, "foi aprovado")
else:
    print("O aluno", aluno, "foi reprovado")
------------------------------------------------
(30) Conversao Real para Dolar

valorReal = input("Valor em Real: ")
cotacao = input("Digite o valor da cotaçao: ")
valorDolar = float(valorReal) * float(cotacao)
print("O valor em dolar é: ",valorDolar)

-----------------------------------------------
(31) Digite um valor inteiro e imprima o seu sucessor e antecessor

valor1 = input("Digite um valor: ")
resultado1 = int(valor1) - 1
resultado2 = int(valor1) + 1
print(resultado1, "é" , resultado2)
---------------------------------------------
(32) calcule a soma do triplo do sucesso mais o dobro do antecessor

valor1 = input("Digite um valor: ")
resultado = ((int(valor1)+1)*3) + ((int(valor1)-1)*2)
print(resultado)

----------------------------------------------
(37) Calcule o valor de um produto com desconto de 12%

valorP = input("Digite o valor produto: ")
valorF = float(valorP) * 0.88
print(valorF)

--------------------------------------------
(38) Digite um salario e de um aumento de 25%
salario01 = input("Digite o salario: ")
novoSalario = float(salario01) * 1.25
print(novoSalario)

--------------------------------------------
Valor total 780000 - ganhador1 46% ganhador2 32% e ganhardor3 22%

valorTotal = float(780000.00)

ganhador1 = float(valorTotal) * 0.46
ganhador2 = float(valorTotal) * 0.32
ganhador3 = float(valorTotal) - float(ganhador1) - float(ganhador2)
print("Valor de ganhador1 é:",ganhador1, "valor de ganhador2 e :", ganhador2,"Valor de ganhador3 é:",ganhador3)

--------------------------------------------
(40) Calcule o salario de um encanador sabendo que valor da diaria e 30 descontando 8% imposto
diariaP = 30
numerodiasT = input("Digite o numero de dias trabalhados: ")
valorBruto = float(diariaP) * float(numerodiasT)
valorLiquido = float(valorBruto)* 0.92
print("O valor bruto é R$:",valorBruto)
print("O valor liquido a receber é R$: ", valorLiquido)

--------------------------------------------
(41) Digite o valor por hora, numero de horas trabalhadas mes, salario a ser recebido acrescido de 10%

valorPhora = input("Digite o valor por hora de trabalho: ")
numeroHtrabalhadas = input("Digite o numero horas trabalhadas: ")
salario = float(valorPhora) * float(numeroHtrabalhadas) * 1.10
print("O seu salario será:",salario)
--------------------------------------------
(42) Calcule o valor a receber sabendo que abate 7% salario base e ganha 5% de gratificação
salarioBase = input("Digite o valor salario base: ")
gratificacao = float(salarioBase) * 0.05
salarioReceber =  float(salarioBase) * 0.93 + float(gratificacao)
print("Seu salario a receber é: ", salarioReceber)

--------------------------------------------
(43) Calcule o valor a vista, parcelas em 3x, comissao a vista e comissa parcelada

valorVenda = input("Digite o valor de venda: ")
pagamentoAvista =  float(valorVenda) * 0.90
valorParcela = float(valorVenda) / 3
comissaoAvista = float(pagamentoAvista) * 0.05
comissaoPrazo = float(valorVenda) * 0.05
print("Pagamento a vista: ",pagamentoAvista)
print("Valor de cada parcela em 3x é: ", valorParcela)
print("Comissao pagamento a vista: ", comissaoAvista)
print("Comissao pagamento a prazo: ", comissaoPrazo)

---------------------------------------------

calcule numeros de degraus a ser subido

alturaDegrau = input("Digite a altura do degrau: ")
alturaAlcancada =  input("Altura final: ")
resultado = float(alturaAlcancada) / float(alturaDegrau)
print("numero de degraus que tera que subir: ",resultado)
-------------------------------------------

Usando Upper, lower, titlte

nome = input("Digite o seu nome: ")
print(nome.title())

-------------------------------------------

(46) Inverter um numero inteiro de 3 digitos
numero = input("Digite um numero inteiro 3 digitos")
resposta = (numero[::-1])

print(resposta)


numero = int(input("Digite um numero inteiros de 4 digitos: "))
n = str(numero)
print(n.split())

(47) Digite um numero de 4 digitos e imprima 1 digito por linha

num = input("Digite um numero de 4 digitos: ")

for n in num:
    print(n)

--------------------------------------------
(48) Digite um valor em segundo e ache a hora em hora minutos e segundo

import math
valor1 = input("Digite um valor inteiro em segundos: ")
valorH = float(valor1) / 3600
restoh = float(valor1) % 3600
valorM = float(restoh) / 60
restoS = float(valorM * 60) % 60
print(int(valorH),":", int(valorM),":",int(restoS))

--------------------------------------------


horaInicial = input("Digite a hora inicial:")
minutoInicial = input("Digite o minuto inicial: ")
segundoInicial = input("digite o segundo incial")
duracaoTrabalho = 6547
horafinal = float(duracaoTrabalho) / 3600
minutoFinal = (float(horafinal) - int(horafinal)) * 60
segundoFinal = ((float(minutoFinal)) - int(minutoFinal)) * 60
print(int(horafinal), int(minutoFinal), int(segundoFinal))

'''

numero = input("Digite um numero inteiro 3 digitos")
resposta = (numero[::-1])

print(resposta)

print(numero[0:1])










