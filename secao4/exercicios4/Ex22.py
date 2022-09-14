"""
# j = jardas and m = metros
while True:
    print('='* 50,'CONVERSOR: JARDAS PARA METROS','='* 50 )
    j = float(input('Informe o valor em jardas:'))
    m = 0.91 * j
    print(f'{j} jardas são iguais a {m:.2f} metros!')
"""

while True:
    print('%' * 50, 'Conversor: Jardas para metros', '%' * 50)
    j = float(input(f'Insira o valor das jardas:'))
    m = 0.91 * j
    print(f'{j} jardas são iguais a {m} metros.')
