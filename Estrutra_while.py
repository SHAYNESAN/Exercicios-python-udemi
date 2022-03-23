'''
loop while
forma geral
While expressao-booleana
    //execução do loop
O bloco do while sera repetido enquanto a expressao booleana for verdadeira
Expressao Booleana é toda expressao onde o resultado e verdadeira ou falso

Exemplo 1 de While, cuidade com loop infinito
numero = 1
while numero < 10:
    print(numero)
    numero = numero + 1
# Obs: Em um loop while, e importante que cuidemos do criterio de parada
'''
resposta = ''
while resposta != 'sim':
    resposta = input('Ja acabou jessica:')
