"""
while True:
    num = float(input('Informe um número real:'))
    if num >=0:
        raiz_quadrada = num ** 1/2
        print(f'A raiz quadrada do número {num} é {raiz_quadrada:.2f}')
        print('=' * 175)
    else:
        quadrado = num ** 2
        print(f'O quadrado do número {num} é {quadrado:.2f}')
"""

while True:
    print('%' * 150)
    num = float(input('Insira um número real:'))
    if num > 0:
        raiz_quadrada = num ** 0.5
        print(f'{raiz_quadrada:.1f} é a raiz quadrada de {num}.')
    else:
        quadrado_do_numero = num ** 2
        print(f'{quadrado_do_numero:.1f} é o quadrado de {num}.')
