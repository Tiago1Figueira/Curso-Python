"""
print('=' * 50, 'CÁLCULO PREÇO FINAL DO PRODUTO', '=' *50)
print('Estado de destino:\n1- Minas Gerais\n2- São Paulo\n3- Mato Grosso\n4- Rio de Janeiro\n5- Sair')
opc = int(input('Opção n°:'))
while opc < 1 or opc > 5:
    print('Atenção: Estado Inválido!\n')
    print('Estado de destino:\n1- Minas Gerais\n2- São Paulo\n3- Mato Grosso\n4- Rio de Janeiro\n5- Sair')
    opc = int(input('Opção n°:'))

valor_produto = float(input('Informe o valor do produto:'))
while True:
    if opc == 1:
        valor_final = valor_produto + (valor_produto * 7/100)
        print(f'O valor final do produto é {valor_final}!\n')
    if opc == 2:
        valor_final = valor_produto + (valor_produto * 12 / 100)
        print(f'O valor final do produto é {valor_final}!\n')
    if opc == 3:
        valor_final = valor_produto + (valor_produto * 8 / 100)
        print(f'O valor final do produto é {valor_final}!\n')
    if opc == 4:
        valor_final = valor_produto + (valor_produto * 15 / 100)
        print(f'O valor final do produto é {valor_final}!\n')
    if opc == 5:
        print('Você saiu!!')
        break
"""
mg = 0.07
sp = 0.12
rj = 0.15
ms = 0.08
while True:
    print('%' * 150)
    print('OPÇÕES:\n1- MG\n2- SP\n3- RJ\n4- MS\n5- SAIR\n')
    opc = float(input('Insira o nº: '))

    if opc == 1:
        produto = float(input('Qual é o valor do produto:'))
        valor_mg = produto + (produto * mg)
        print(f'{valor_mg:.2f} reais é o valor final do produto para Minas Gerais.')

    elif opc == 2:
        produto = float(input('Qual é o valor do produto:'))
        valor_sp = produto + (produto * sp)
        print(f'{valor_sp:.2f} reais é o valor final do produto para São Paulo.')

    elif opc == 3:
        produto = float(input('Qual é o valor do produto:'))
        valor_rj = produto + (produto * rj)
        print(f'{valor_rj:.2f} reais é o valor final do produto para Rio de Janeiro.')

    elif opc == 4:
        produto = float(input('Qual é o valor do produto:'))
        valor_ms = produto + (produto * ms)
        print(f'{valor_ms:.2f} reais é o valor final do produto para Mato Grosso do Sul.')

    elif opc == 5:
        print('Você saiu!!')
        break

    else:
        print('Valor inválido!\nFavor inserir valores entre 1 e 5!')
