"""
while True:
    print("=" * 50, 'CALCULE A ÁREA DO QUADRADO', "=" * 50)
    num = float(input('Informe a medida do lado do quadrado:'))
    area = num * num
    print(f'A área do quadrado de lado {num} é {area:.2f}!')
"""

while True:
    print('%' * 50, 'Área do quadrado', '%' * 50)
    lado = float(input('Insira o valor do lado:'))
    print(f'A área desse quadrado é {lado * lado:.2f}')
