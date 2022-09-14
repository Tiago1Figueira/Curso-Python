"""
#k = km/h
#m = m/s
while True:
    print('=' * 50, 'CONVERSOR: KM/H PARA M/S', '=' * 50)
    k = float(input('Informe a velocidade em km/h:'))
    m = k / 3.6
    print(f'{k} quilômetros por horas são iguais a {m:.2f} metros por segundo.')
"""

while True:
    k = float(input(f'Insira o número em quilômetros:'))
    ms = k / 3.6
    print(f'O valor de {k} quilômetros é igual a {ms:.3} metros/segundo.')

