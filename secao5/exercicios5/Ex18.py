"""
#se eu coloco mais de um número inválido sucessivamente(menor que 1 ou maior q 5) o programa deixa de falar
#'número inválido' vez sim e vez não. Pq?
print('=' * 50, 'CÁLCULO DE OPERAÇÕES MATEMÁTICAS', '=' * 50)
print('Opções:\n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Sair\n')
opt = int(input('Selecione um número: n°'))

while True:
    if opt < 1 or opt > 5:
        print('Número inválido!')
        print('Opções:\n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Sair\n')
        opt = int(input('Selecione um número: n°'))

    if opt == 1:
        num1 = int(input('Informe o 1° valor da soma:'))
        num2 = int(input('Informe o 2° valor da soma:'))
        soma = num1 + num2
        print(f'A soma dos números {num1} e {num2} é igual a {soma}')

    if opt == 2:
        num1 = int(input('Informe o 1° valor da subtração:'))
        num2 = int(input('Informe o 2° valor da subtração:'))
        subtracao = num1 - num2
        print(f'A subtração dos números {num1} e {num2} é igual a {subtracao}')

    if opt == 3:
        num1 = int(input('Informe o 1° valor da multiplicação:'))
        num2 = int(input('Informe o 2° valor da multiplicação:'))
        multiplicacao = num1 * num2
        print(f'A multiplicação dos números {num1} e {num2} é igual a {multiplicacao}')

    if opt == 4:
        num1 = int(input('Informe o 1° valor da divisão:'))
        num2 = int(input('Informe o 2° valor da divisão:'))
        subtracao = num1 / num2
        print(f'A divisão dos números {num1} e {num2} é igual a {subtracao}')

    if opt == 5:
        print('Você saiu!')
        break
"""
while True:
    print('%' * 50, 'CÁLCULO DE OPERAÇÕES MATEMÁTICAS:', '%' * 50)
    print('Opções: \n 1- adição\n 2- subtração\n 3- multiplicação\n 4- divisão\n 5- sair \n')
    opt = float(input('Insira um número de opção - nº:')) # coloca-se float e não int pra não dar erro c/ nº decimal.

    while opt < 1 or opt > 5:
        print('Número inválido!')
        opt = float(input('Insira um número de opção - nº:'))
    if opt == 1:
        adicao1 = float(input('Insira o 1º número da adição:'))
        adicao2 = float(input('Insira o 2º número da adição:'))
        adicao = adicao1 + adicao2
        print(f'O valor da adição é {adicao}.')
    elif opt == 2:
        subtracao1 = float(input('Insira o 1º número da subtração:'))
        subtracao2 = float(input('Insira o 2º número da subtração:'))
        subtracao = subtracao1 - subtracao2
        print(f'O valor da subtração é {subtracao}.')
    elif opt == 3:
        multiplicao1 = float(input('Insira o 1º número da multiplição:'))
        multiplicao2 = float(input('Insira o 2º número da multiplição:'))
        multiplicao = multiplicao1 * multiplicao2
        print(f'O valor da multiplição é {multiplicao}.')
    elif opt == 4:
        divisao1 = float(input('Insira o 1º número da divisão:'))
        divisao2 = float(input('Insira o 2º número da divisão:'))
        divisao = divisao1 / divisao2
        print(f'O valor da divisão é {divisao}.')
    elif opt == 5:
        print('Você saiu!')
        break
    else:
        print('Número inválido! Você saiu!')
        break
