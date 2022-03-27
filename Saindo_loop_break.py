'''
Saindo de loops com break
funciona da mesma forma que nas liguagens C ou Java.
Utilizamos o break para sair de loops de maneira projetada
'''

for numero in range(1, 11):
    if numero ==6:
        break
    else:
        print(numero)
print('Sai do loop')

# Exemplo 2
while True:
    comando = input("Digite 'sair' para finalizar: ")
    if comando == 'sair':
        break
    