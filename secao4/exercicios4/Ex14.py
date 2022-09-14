"""
#g = ângulo
# r = radianos
pi = 3.14
while True:
    print('=' * 50, 'CONVERSOR: GRAUS EM RADIANOS!', '=' * 50)
    g = float(input('Informe o valor do ângulo que deseja converter:'))
    r = g * pi / 180
    print(f'{g} graus são {r:.2f} radianos!!')
"""
while True:
    print('#'*50,'Conversor graus para radianos', '#'*50)
    pi = 3.14
    g = float(input(f'Insira a quantidade de graus:'))
    r = g * pi/180
    print(f'{g} graus são iguais a {r:.2} radianos.')

