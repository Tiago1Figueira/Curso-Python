"""
while True:
    print('='*50,'ESCOLHA UMA OPERAÇÃO','='*50)
    print('Opções:\n1-Geométrica\n2-Ponderada\n3-Harmônica\n4-Aritmética\n5-Sair')
    opc = int(input('N°:'))
    if opc < 1 or opc > 5:
        print('Atenção: número inválido!')
        print('Opções:\n1-Geométrica\n2-Ponderada\n3-Harmônica\n4-Aritmética\n5-Sair')
        opc = int(input('N°:'))
    if opc == 1:
        x = int(input('Informe X:'))
        y = int(input('Informe Y:'))
        z = int(input('Informe Z:'))
        geometrica = (x*y*z) ** 1/3
        print(f'A média geométrica dos números {x}, {y}, {z} é igual a {geometrica:.2f}!')
    if opc == 2:
        x = int(input('Informe X:'))
        y = int(input('Informe Y:'))
        z = int(input('Informe Z:'))
        ponderada = (x+2 * y+3 * z) / 6
        print(f'A média ponderada dos números {x}, {y}, {z} é igual a {ponderada:.2f}!')
    if opc == 3:
        x = int(input('Informe X:'))
        y = int(input('Informe Y:'))
        z = int(input('Informe Z:'))
        harmonica =  1 / 1/x + 1/y + 1/z
        print(f'A média harmônica dos números {x}, {y}, {z} é igual a {harmonica:.2f}!')
    if opc == 4:
        x = int(input('Informe X:'))
        y = int(input('Informe Y:'))
        z = int(input('Informe Z:'))
        aritmetica = (x + y+ z) / 3
        print(f'A média aritmética dos números {x}, {y}, {z} é igual a {aritmetica:.2f}!')
    if opc ==5:
        print('Você saiu!')
        break
"""
while True:
    print('%' * 50, 'CÁLCULO DAS MÉDIAS', '%' * 50)
    print('OPÇÕES:\n1- MÉDIA GEOMÉTRICA:\n2- MÉDIA PONDERADA:\n3- MÉDIA HARMÔNICA:\n4- ARITMÉTICA:\n5- SAIR:')
    media = float(input('Insira um opção - Nº:'))
    while media != 1 and media != 2 and media != 3 and media != 4 and media != 5:
        print('Número inválido:')
        media = float(input('Insira um opção - Nº:'))
    if media == 1:
        x = int(input('Informe valor X:'))
        y = int(input('Informe valor Y:'))
        z = int(input('Informe valor Z:'))
        geometrica = (x * y * z) ** 1 / 3
        print(f'Média Geométrica igual a {geometrica:.2f}!')
    elif media == 2:
        x = int(input('Informe valor X:'))
        y = int(input('Informe valor Y:'))
        z = int(input('Informe valor Z:'))
        ponderada = (x + 2 * y + 3 * z) / 6
        print(f'Média Ponderada é igual a {ponderada:.2f}!')
    elif media == 3:
        x = int(input('Informe valor X:'))
        y = int(input('Informe valor Y:'))
        z = int(input('Informe valor Z:'))
        harmonica = 1 / (1 / x + 1 / y + 1 / z)
        print(f'Média Harmônica é igual a {harmonica:.2f}!')
    elif media == 4:
        x = int(input('Informe valor X:'))
        y = int(input('Informe valor Y:'))
        z = int(input('Informe valor Z:'))
        aritmetica = x + y + z / 3
        print(f'Média Aritmética é igual a {aritmetica:.2f}!')
    elif media == 5:
        print('Você saiu!')
        break
    else:
        print('Valor inválido! Você saiu!')
        break
