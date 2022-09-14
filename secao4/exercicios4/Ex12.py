"""
#quilômetros = k
# milhas = m
while True:
    print('=' * 50, 'CONVERSOR: MILHAS PARA QUILÔMETROS:', '=' * 50)
    m = int(input('Informe o valor em milhas:'))
    km = m * 1.6
    print(f'O valor de {m} milhas em quilômetros é igual a {km}!!')
"""

m = float(input(f'Insira a quantidade de milhas:'))
k = 1.61 * m
print(f'{m} milhas são iguais a {k} quilômetros.')
