"""
#1
divisivel_11 = 0
divisivel_13 = 0
divisivel_17 = 0
num = int(input('Informe um número:'))
for i in range(num, num + 17):
    if i > num:
        if i % 11 == 0:
            divisivel_11 = i
        if i % 13 == 0:
            divisivel_13 = i
        if i % 17 == 0:
            divisivel_17 = i
print(f'Após o número {num} os números divisíveis por 11, 13 e 17 são respectivamente '
      f'{divisivel_11}, {divisivel_13} e {divisivel_17}.')
# erro: quando se coloca o número 34 o valor de primeiro múltiplo de 17 após esse número aparece como 0.
# o que devo fazer para acertar o código? 

#2
divisivel_11 = 0
divisivel_13 = 0
divisivel_17 = 0
num = int(input('Informe um número:'))
for i in range(num, num + 20):
    if i > num:
        if i % 11 == 0:
            divisivel_11 = i
        if i % 13 == 0:
            divisivel_13 = i
        if i % 17 == 0:
            divisivel_17 = i
print(f'O divisores de 11, 13 e 17 após o número {num} são {divisivel_11}, {divisivel_13}, {divisivel_17}!')

#3
divisor_11 = ' '
divisor_13 = ' '
divisor_17 = ' '
while True:
    num = float(input('Informe um número:'))
    while num < 0 or num != int(num):
        print('Número inválido!')
        num = float(input('Informe um número:'))
    for i in range(int(num), int(num) + 18):
        if i > num:
            if i % 11 == 0:
                divisor_11 = i
            elif i % 13 == 0:
                divisor_13 = i
            elif i % 17 == 0:
                divisor_17 = i
    print(f'Os primeiros divisores por 11, 13 e 17 após o número {num} são {divisor_11}, {divisor_13} e {divisor_17}!')


div_11 = 0
div_13 = 0
div_17 = 0
while True:
    print('%' * 50, 'CALCULA OS 3 PRIMEIROS VALORES DIVISORES DE 11,13 E 17 '
                    'DEPOIS DO NÚMERO RECEBIDO:', '%' * 50)
    num = float(input('Insira um número inteiro:'))
    while num != int(num):
        print('Número inválido!')
        num = float(input('Insira um número inteiro:'))
    for i in range(0, int(num) + 18):
        if i % 11 == 0:
            div_11 = i
        elif i % 13 == 0:
            div_13 = i
        elif i % 17 == 0:
            div_17 = i
    print(f'Os primeiros divisores de 11, 13 e 17 após {num} são '
          f'{div_11}, {div_13} e {div_17} respectivamente.')

"""
divisor11 = ''
divisor13 = ''
divisor17 = ''
while True:
    print('%' * 50, 'CALCULA OS 3 PRIMEIROS VALORES DIVISORES DE 11,13 E 17 '
                    'DEPOIS DO NÚMERO RECEBIDO:', '%' * 50)
    num = float(input('Insira um número inteiro e positivo:'))
    while num != int(num) or num <= 0:
        print('Número inválido!')
        num = float(input('Insira um número inteiro e positivo:'))
    num = int(num)
    for i in range(num, num + 18):
        if i % 11 == 0:
            divisor11 = i
        if i % 13 == 0:
            divisor13 = i
        if i % 17 == 0:
            divisor17 = i
    print(f'Os primeiros divisores de 11, 13, 17 depois do '
          f'número {num} são respectivamente '
          f'{divisor11},{divisor13},{divisor17}')
