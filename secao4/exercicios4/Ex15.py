"""
#g = ângulo
# r = radianos
pi = 3.14
while True:
    print('=' * 50, 'CONVERSOR: RADIANOS EM GRAUS!', '=' * 50)
    r = float(input('Informe o valor dos radianos que deseja converter:'))
    g = r * 180 / pi
    print(f'{r} radianos são {g:.2f} graus!!')
"""
while True:
    print('%'*50, 'Conversor radianos para graus', '%'*50)
    pi = 3.14
    r = float(input(f'Insira a quantidade de radianos:'))
    g = r * 180 / pi
    print(f'{r} radianos são iguais a {g:.6} graus. ')

