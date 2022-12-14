"""
while True:
    num = int(input('Informe um número positivo:'))
    if num < 0:
        print('Atenção: número negativo! ')
        num = int(input('Informe um número positivo:'))
    else:
        raiz_quadrada = num ** 1/2
        quadrado = num ** 2
        print(f'O número {num} tem raiz quadrada igual a {raiz_quadrada} e seu quadrado é {quadrado}!')
"""
while True:
    print('%' * 150)
    num = float(input('Insira um número:'))
    if num > 0:
        print(f'número dado:{num};  quadrado: {num ** 2:.2f}; raiz quadrada: {num ** 0.5:.2f};')
        # print(f'{num ** 2:.2f} é o quadrado de {num} e {num ** 0.5:.2f} é a sua raiz quadrada.')
    else:
        print('Favor informar número positivo!')
