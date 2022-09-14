"""
valor_pagar = ' '
qtd = ' '
while True:
    print('='*50, 'CALCULE O VALOR A PAGAR', '=' *50)
    codigo = float(input('Informe o código do produto:'))
    while codigo < 100 or codigo > 106:
        print('Código inválido!')
        codigo = float(input('Informe o código do produto:'))
    qtd = int(input('Informe a quantidade a ser consumida:'))
    while qtd <= 0:
        print('Quantidade Inválida!')
        qtd = int(input('Informe a quantidade a ser consumida:'))

    if codigo == 100:
        valor_pagar = 1.20 * qtd
        print(f'{qtd} Cachorros Quentes - Valor a pagar = {valor_pagar:.2f}! ')
    if codigo == 101:
        valor_pagar = 1.30 * qtd
        print(f'{qtd} Bauru Simples - Valor a pagar = {valor_pagar:.2f}! ')
    if codigo == 102:
        valor_pagar = 1.50 * qtd
        print(f'{qtd} Bauru com ovo - Valor a pagar = {valor_pagar:.2f}! ')
    if codigo == 103:
        valor_pagar = 1.20 * qtd
        print(f'{qtd} Hamburguer - Valor a pagar = {valor_pagar:.2f}! ')
    if codigo == 104:
        valor_pagar = 1.70 * qtd
        print(f'{qtd} Cheese Burguer - Valor a pagar = {valor_pagar:.2f}! ')
    if codigo == 105:
        valor_pagar = 2.20 * qtd
        print(f'{qtd} Suco - Valor a pagar = {valor_pagar:.2f}! ')
    if codigo == 106:
        valor_pagar = 1.00 * qtd
        print(f'{qtd} Refrigerante - Valor a pagar = {valor_pagar:.2f}! ')
"""
while True:
    print('%' * 150)
    codigo = int(input('Informe o código do produto:'))
    while codigo != 100 and codigo != 101 and codigo != 102 and codigo != 103 and codigo != 104 and codigo != 105 and codigo != 106:
        print('Número inválido!')
        codigo = int(input('Informe o código do produto:'))
    qtd = int(input('Informe a quantidade que irá comprar:'))
    while qtd <= 0:
        print('Quantidade inválida!')
        qtd = int(input('Informe a quantidade que irá comprar:'))
    if codigo == 100:
        valor0 = 1.20 * qtd
        print(f'Total a pagar é {valor0:.2f}')
    elif codigo == 101:
        valor1 = 1.30 * qtd
        print(f'Total a pagar é {valor1:.2f}')
    elif codigo == 102:
        valor2 = 1.50 * qtd
        print(f'Total a pagar é {valor2:.2f}')
    elif codigo == 103:
        valor3 = 1.20 * qtd
        print(f'Total a pagar é {valor3:.2f}')
    elif codigo == 104:
        valor4 = 1.70 * qtd
        print(f'Total a pagar é {valor4:.2f}')
    elif codigo == 105:
        valor5 = 2.20 * qtd
        print(f'Total a pagar é {valor5:.2f}')
    elif codigo == 106:
        valor6 = 1.00 * qtd
        print(f'Total a pagar é {valor6:.2f}')
    else:
        print('Código inválido! Você saiu!')
        break
