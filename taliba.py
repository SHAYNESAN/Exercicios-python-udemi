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
----------------------------------------------------------------

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
