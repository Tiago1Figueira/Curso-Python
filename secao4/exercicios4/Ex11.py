"""
#km/h = k
# m/s = m
while True:
    print('=' * 50, 'CONVERSOR: M/S PARA KM/H', '=' * 50)
    m = int(input('Informe o valor em metros por segundo:'))
    k = m * 3.6
    print(f'O valor de {m} m/s em km/h é igual a {k}!!')
"""

while True:
    ms = float(input(f'Informe quantos metros por segundo serão convertidos:'))
    k = ms * 3.6
    print(f'{ms} m/s são iguais a {k} km/h.')
