"""
#1
comissao1 = 0.05
imposto1 = 0.00
comissao2 = 0.10
imposto2 = 0.15
comissao3 = 0.15
imposto3 = 0.20
while True:
    print('='*150)
    custo_fabrica = float(input('Informe o valor do custo de fábrica:'))
    if custo_fabrica < 12000:
        comissao = custo_fabrica * comissao1
        imposto = custo_fabrica * imposto1
    elif custo_fabrica >= 12000 and custo_fabrica <= 25000:
        comissao = custo_fabrica * comissao2
        imposto = custo_fabrica * imposto2
    else:
        comissao = custo_fabrica * comissao3
        imposto = custo_fabrica * imposto3
    print(f'Custo de fábrica {custo_fabrica:.2f}\ncomissão do distribuidor {comissao:.2f}\nimpostos {imposto:.2f}')
"""
comissao1 = 0.05
comissao2 = 0.10
comissao3 = 0.15
imposto1 = 0
imposto2 = 0.15
imposto3 = 0.20
while True:
    print('%' * 50, 'CÁLCULO DO CUSTO DE UM CARRO AO CONSUMIDOR:', '%' * 50)
    custo_de_fabrica = float(input('Insira o valor do custo de fábrica do carro: R$'))
    if custo_de_fabrica <= 1200:
        valor_carro1 = custo_de_fabrica + (custo_de_fabrica * imposto1) + (custo_de_fabrica * comissao1)
        print(f'O valor do carro ao consumidor será R$ {valor_carro1:.2f}.')
    elif custo_de_fabrica > 1200 and custo_de_fabrica <= 2500:
        valor_carro2 = custo_de_fabrica + (custo_de_fabrica * imposto2) + (custo_de_fabrica * comissao2)
        print(f'O valor do carro ao consumidor será R$ {valor_carro2:.2f}')
    else:
        valor_carro3 = custo_de_fabrica + (custo_de_fabrica * imposto3) + (custo_de_fabrica * comissao3)
        print(f'O valor do carro ao consumidor será R$ {valor_carro3:.2f}')







