'''
Ranges
precisamos conhecer o loop for para usar os ranges
precisamos conhecer o range para trabalhar melhor com loops for
Ranges sao utulizados para gerar sequencias numerias, nao de formas aleatorias
formas gerais:
range(valor_de_parada)
obs: valor_de_parada nao inclusiva
#forma 1
for num in range(11):
    print(num)

#forma 2 começa em um determinado lugar

for num in range(1, 11):
    print(num)

#forma 3 range(valor_inicio, _valor-de-parada) e passo especificado pelo usuario
for num in range(1, 10, 2):
    print(num)

forma 4 (inversa)
'''
for num in range(10, 0, -1):
    print(num)
