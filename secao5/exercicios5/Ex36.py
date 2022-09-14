"""
porc1 = 0.16
base1 = 700
porc2 = 0.14
base2 = 650
porc3 = 0.14
base3 = 600
porc4 = 0.14
base4 = 550
porc5 = 0.14
base5 = 500
porc6 = 0.14
base6 = 400

while True:
    print('=' * 50, 'CALCULE A COMISSÃO', '=' * 50)
    venda = float(input('Informe o valor da venda:'))
    if venda >= 100000:
        comissao = ( venda * porc1) + base1
        print(f'A comissão será de {comissao:.2f}')
    elif venda < 100000 and venda >= 80000:
        comissao = ( venda * porc2) + base2
        print(f'A comissão será de {comissao:.2f}')
    elif venda < 80000 and venda >= 60000:
        comissao = ( venda * porc3) + base3
        print(f'A comissão será de {comissao:.2f}')
    elif venda < 60000 and venda >= 40000:
        comissao = ( venda * porc4) + base4
        print(f'A comissão será de {comissao:.2f}')
    elif venda < 40000 and venda >= 20000:
        comissao = ( venda * porc5) + base5
        print(f'A comissão será de {comissao:.2f}')
    else:
        comissao = ( venda * porc6) + base6
        print(f'A comissão será de {comissao:.2f}')
"""
valor_fixo1 = 400
porcentagem1= 0.14
valor_fixo2 = 500
porcentagem2 = 0.14
valor_fixo3 = 550
porcentagem3 = 0.14
valor_fixo4 = 600
porcentagem4 = 0.14
valor_fixo5 = 650
porcentagem5 = 0.14
valor_fixo6 = 700
porcentagem6 = 0.16
while True:
    print('%' * 150)
    venda = float(input('Qual é o valor da venda:'))
    if venda < 20_000:
        comissao1 = valor_fixo1 + (venda * porcentagem1)
        print(f'O valor da comissão será de {comissao1:.2f}')
    elif venda >= 20_000 and venda < 40_000:
        comissao2 = valor_fixo2 + (venda * porcentagem2)
        print(f'O valor da comissão será de {comissao2:.2f}')
    elif venda >= 40_000 and venda < 60_000:
        comissao3 = valor_fixo3 + (venda * porcentagem3)
        print(f'O valor da comissão será de {comissao3:.2f}')
    elif venda >= 60_000 and venda < 80_000:
        comissao4 = valor_fixo4 + (venda * porcentagem4)
        print(f'O valor da comissão será de {comissao4:.2f}')
    elif venda >= 80_000 and venda < 100_000:
        comissao5 = valor_fixo5 + (venda * porcentagem5)
        print(f'O valor da comissão será de {comissao5:.2f}')
    else:
        comissao6 = valor_fixo6 + (venda * porcentagem6)
        print(f'O valor da comissão será de {comissao6:.2f}')


