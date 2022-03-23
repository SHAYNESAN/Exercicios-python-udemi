'''
Estruturas logica: and, or, not. is
Operadores unarios
    not
Operadores binarios
    and - or - is
Para o 'and' ambos os valores precisam ser True
ativo = True
logado = False
if ativo and logado:
    print('Bem vindo usuario')

else:
    print('Voce precisar ativar a sua conta')
-------------------------------------------------
Para o 'or' um ou outro precisa ser True
ativo = False
logado = True
if ativo or logado:
    print('Bem vindo usuario')

else:
    print('Voce precisar ativar a sua conta')
-----------------------------------------------

Para o not o valor do booleano e invertido
'''

ativo = False
logado = True
if not logado:
    print('Voce precisa logar? ')

else:
    print('Bem vindo usuario')



