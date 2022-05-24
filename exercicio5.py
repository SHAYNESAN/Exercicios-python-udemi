'''
exec-1
num1 = input('digite 1 numero:')
num2 = input('Digite o 2 numero:')
if num1 > num2:
    print('O numero maior é:', num1)
else:
    print('O numero maior é:', num2)
---------------------------------------
exec-2
num = (input('Digite um numero: '))
if num >= "0":
    print(float(num) ** (1/2))
else:
    print('Não existe raiz quadrada de número negativo')
---------------------------------------
exec-3
num = (input('Digite um numero: '))
if num >= "0":
    print(float(num) ** (1/2))
else:
    print(float(num) ** (2))
---------------------------------------
exec-4
num = (input('Digite um numero: '))
if num >= "0":
    print(float(num) ** (1/2))
    print(float(num) ** (2))
------------------------------------------
exec-5 
num = int(input('Digite um numero: '))
if num % 2 == 0:
    print('O numero é par')
else:
    print('O numero é impar')

--------------------------------------
exec-6
num1 = int(input('Digite 1 numero: '))
num2 = int(input('Digite o 2 numero: '))
if num1 > num2:
    print('O numero maior é:', num1)
    print('A diferenca dos numeros e:', num1 - num2)
else:
    print('O numero maior é:', num2)
    print('A diferenca dos numeros e:', num2 - num1)
    
------------------------------------------------   
exec-7 
num1 = input('Digite 1 numero: ')
num2 = input('Digite o 2 numero: ')

if num1 > num2:
    print('O numero maior é:', num1)

elif num1 < num2:
    print('O numero maior é:', num2)

elif num1 == num2:
    print('Os numeros são iguais')
--------------------------------------------
exec-8

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
if (nota1 >= 0 and nota1 <= 10) and (nota2 >= 0 and nota2 <= 10):
    media = (nota1 + nota2) / 2
    print('A media é:', media)
else:
    print('Nota invalida')
    
------------------------------------------------------
exec-9

salario = float(input('Digite o salario: '))
prestacao = float(input('Digite a prestacao: '))
if prestacao > salario * 0.20:
    print('O emprestimo foi negado')
else:
    print('O emprestimo foi aprovado')

-------------------------------------------------
exec-10
altura = float(input('Digite a altura: '))
peso = float(input('Digite o peso: '))
sexo = input('Digite o sexo: ')
if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print('O peso ideal é:', peso_ideal)

if sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print('O peso ideal é:', peso_ideal)

------------------------------------------
exec-11

num = input('Digite um numero: ')
soma = 0
if float(num) > 0:
    for n in num:
        soma = soma + int(n)
    print(f'A soma dos Algoritimos de {num} é {soma}')
else:
    print(f'Numero invalido:') 
------------------------------------------------
exec-12
import math
num = int(input('Digite um numero: '))
if num >= 0:
    resultado = math.log(num, 10)    
    print(resultado)
else:
    print('Numero invalido')
------------------------------------------
exec-13 

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
resultado = (nota1 * 1) + (nota2 * 1) + (nota3 * 2)
media_ponderada = resultado / 3
print('A media é:', media_ponderada)
if media_ponderada >= 60:
    print('Aprovado')
else:
    print('Reprovado')
-------------------------------------------
exec-14
nota_trabalho = float(input('Digite a nota do trabalho : '))
avaliacao_semestral = float(input('Digite a avaliacao semestral: '))
exame_final = float(input('Digite o exame final : '))
resultado = (( nota_trabalho   + avaliacao_semestral   + exame_final )  / 3)
print('A media é:', resultado)

if (resultado == 0 or resultado <= 2.9):
    print('Sua nota e Reprovado')

elif resultado == 3 or resultado <= 4.9:
    print('Recuperacao')

else:
    print('Aprovado')
-------------------------------------------
exec-17
base_maior = float(input('Digite a base maior: '))
base_menor = float(input('Digite a base menor: '))
altura = float(input('Digite a altura: '))
Area_trapezio = ((base_maior + base_menor) * altura) / 2
print('A area do trapezio é:', Area_trapezio)
--------------------------------------------
exec-18

operacoes = input('Digite a operacao: (Soma) (Subtracao) (Multiplicacao) (Divisao) ')
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if operacoes == "Soma":
    Soma = num1 + num2
    print('A soma dos numeros e:', Soma)
elif operacoes == "Subtracao":
    Subtracao = num1 - num2
    print('A subtracao dos numeros e:', Subtracao)
elif operacoes == "Multiplicacao":
    Multiplicacao = num1 * num2
    print('A multiplicacao dos numeros e:', Multiplicacao)
elif operacoes == "Divisao":
    Divisao = num1 / num2
    print('A divisao dos numeros e:', Divisao)
-------------------------------------------------
exec-19
num1 = int(input('Digite um numero: '))
if num1 % 3 == 0 or num1 % 5 == 0:
    print(num1, 'e divisivel por 3 ou 5')
---------------------------------------------------


lado_a = float(input('Digite o lado a: '))
lado_b = float(input('Digite o lado b: '))
lado_c = float(input('Digite o lado c: '))
equilatero = (lado_a == lado_b == lado_c)
isoceles = (lado_a == lado_b or lado_a == lado_c or lado_b == lado_c)
escaleno = lado_a != lado_b != lado_c
resultado = (equilatero, isoceles, escaleno)
if (lado_b + lado_c < lado_a) or (lado_a + lado_c < lado_b) or (lado_a + lado_b < lado_c):
    print('Os lados nao formam um triangulo')
elif equilatero == True:
        print('O seu Triangulo e equilatero')
elif isoceles == True:
        print('O seu Triangulo e isoceles')
elif escaleno == True:
        print('O seu Triangulo e escaleno')
        
  

Idade =  int(input('Digite a sua idade: '))
tempo_trabalho = int(input('Digite o tempo de trabalho: '))
if Idade >= 65 or tempo_trabalho >= 30 or Idade >= 60 and tempo_trabalho >= 25:
    print('Voce ja pode aposentar')
else:
    print('Vc nao pode se aposentar')


Ano = int(input('Digite o ano: '))
if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0:
    print('Ano bissexto')
else:
    print('Ano nao bissexto')
    

------------------------------------------------------
exec-24

Produto = 130
Estado = input('Digite o estado: ')
if Estado == 'SP':
    Produto_final = Produto + (Produto * 0.12)
    print('O valor do produto com o imposto e:', Produto_final)
elif Estado == 'MG':
    Produto_final = Produto + (Produto * 0.07)
    print('O valor do produto com o imposto e:', Produto_final)
elif Estado == 'RJ':
    Produto_final = Produto + (Produto * 0.15)
    print('O valor do produto com o imposto e:', Produto_final) 
elif Estado == 'MS':
    Produto_final = Produto + (Produto * 0.08)
    print('O valor do produto com o imposto e:', Produto_final)

else:   
    print('Estado invalido') 

-------------------------------

km = float(input('Digite a distancia percorrida: '))
Gasolina_gasta = float(input('Digite o consumo de gasolina gasta: ')) 
consumo = km / Gasolina_gasta
if consumo <= 8:
    print('Seu consumo e :%s km/l' % consumo)
    print('Vende o seu carro')
elif consumo > 8 and consumo <= 14:
    print('Seu consumo e : %s km/l' % consumo)
    print('Econonico')
elif consumo > 14:
    print(f'Seu consumo e : %s km/l' % consumo)
    print('Super econonico')
-----------------------------------------------
exec-25
Idade_atleta = int(input('Digite a sua idade: '))
if Idade_atleta >= 5 and Idade_atleta <= 7:
    print('Infantil A')
elif Idade_atleta >= 8 and Idade_atleta <= 10:    
    print('Infantil B')
elif Idade_atleta >= 11 and Idade_atleta <= 13:
    print('Juvenil A')
elif Idade_atleta >= 14 and Idade_atleta <= 17:
    print('Juvenil B')
elif Idade_atleta >= 18:
    print('Senior')
-------------------------------------------
exec-29

import random
print('Bem vindo a prova de matematica')
print('Voce tera 5 questoes com numeros aleatorios')
resposta = 0 
Resposta_correta = 0
Resposta_errada = 0
while resposta != 5:
    numero = random.randint(1,100)
    numero2 = random.randint(1,100)
    print('O primeiro numero: ',numero)
    print('O segundo numero: ',numero2)
    Resultado = numero + numero2
    Sua_resposta = int(input('Qual e o valor da soma: numero + numero 2: '))
    print('Sua resposta: ',Sua_resposta)
    print('Resultado: ',Resultado)
    if Sua_resposta == numero + numero2:
        print('Voce acertou \n')
        Resposta_correta += 1
    else:
        print('Voce errou \n')
        Resposta_errada += 1
    
    resposta = resposta + 1
print((f'Voce acertou {Resposta_correta} questoes'))
print((f'Voce errou {Resposta_errada} questoes'))
-----------------------------------------------------
exec-30

import random
lista = []
numero1 = random.randint(1,100)
numero2 = random.randint(1,100)
numero3 = random.randint(1,100)
lista = [numero1, numero2, numero3]
print(lista)
lista.sort()
print(lista)

---------------------------------------------------
exec-31
Altura = float(input('Digite a sua altura: '))
Peso = float(input('Digite o seu peso: '))
if Altura < 1.20 and Peso <= 60:
    print('Voce esta na classe A')
elif 1.20 <= Altura <= 1.70 and Peso <= 60:
    print('Voce esta na classe B')
elif 1.70 < Altura  and Peso <= 60:
    print('Voce esta na classe C')

elif Altura < 1.20 and  60 <= Peso <= 90:
    print('Voce esta na classe D')

elif 1.20 <= Altura <= 1.70 and 60 <= Peso <= 90:
    print('Voce esta na classe E')

elif 1.70 < Altura  and 60 <= Peso <= 90:
    print('Voce esta na classe F')

elif Altura < 1.20 and  90 < Peso:
    print('Voce esta na classe G')  

elif 1.20 <= Altura <= 1.70 and 90 < Peso:
    print('Voce esta na classe H')

elif 1.70 < Altura  and 90 < Peso:
    print('Voce esta na classe I')


--------------------------------------------------
exec-32
'''
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

'''

'''
----------------------------------------------------
exec-33

import random
lista = []
numero1 = random.randint(1,100)
numero2 = random.randint(1,100)
numero3 = random.randint(1,100)
lista = [numero1, numero2, numero3]
print(lista)
lista.sort()
print(lista)

---------------------------------------------------

exec-34


Preco_pruduto_novo = 0
Preco_produto = float(input('Digite o preco do produto1: '))
if Preco_produto <= 50:
    Preco_pruduto_novo = Preco_produto + (Preco_produto * 0.05)
elif  50 <= Preco_produto <= 100:
    Preco_pruduto_novo = Preco_produto + (Preco_produto * 0.10)
elif 100 < Preco_produto :
    Preco_pruduto_novo = Preco_produto + (Preco_produto * 0.15)
if Preco_pruduto_novo <=80:
    print('Preco barato ',Preco_pruduto_novo)
elif 80 < Preco_pruduto_novo <= 120:
    print('Preco normal',Preco_pruduto_novo)
elif 120 < Preco_pruduto_novo <=200:
    print('Preco caro',Preco_pruduto_novo)
elif 200 < Preco_pruduto_novo:
    print('Preco muito caro',Preco_pruduto_novo)
-------------------------------------------------
exec-34
Nota = float(input('Digite a sua nota: '))
Faltas = int(input('Digite o numero de faltas: '))
if  9 <= Nota <=  10 and Faltas <= 20:
    print('O seu conceito e A')
elif 7.5 <= Nota <= 8.9 and Faltas <= 20:
    print('O seu conceito e B')
elif 5 <= Nota <= 7.4 and Faltas <= 20:
    print('O seu conceito e C')
elif 4 <= Nota <= 4.9 and Faltas <= 20:
    print('O seu conceito e D')
elif 0 <= Nota <= 3.9 and Faltas <= 20:
    print('O seu conceito e E')
elif  9 <= Nota <=  10 and Faltas >= 20:
    print('O seu conceito e B')
elif 7.5 <= Nota <= 8.9 and Faltas >= 20:
    print('O seu conceito e C')
elif 5 <= Nota <= 7.4 and Faltas >= 20:
    print('O seu conceito e D')
elif 4 <= Nota <= 4.9 and Faltas >= 20:
    print('O seu conceito e E')
elif 0 <= Nota <= 3.9 and Faltas >= 20:
    print('O seu conceito e E')

'''
Dia []