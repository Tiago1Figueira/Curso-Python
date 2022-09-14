"""
#quilômetros = k
# milhas = m
while True:
    print('=' * 50, 'CONVERSOR: QUILÔMETROS PARA MILHAS:', '=' * 50)
    km = float(input('Informe o valor em quilômetros:'))
    m = km / 1.6
    print(f'O valor de {km:.2f} quilômetros em milhas é igual a {m:.2f}!!')
"""
while True:
    print('='* 50, 'Conversor km para milhas', '='*50)
    k = float(input(f'Insira a quantidade de quilômetros:'))
    m = k / 1.61
    print(f'{k} quilômetros são iguais a {m:.4} milhas.')
