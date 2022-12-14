"""
# k = Kelvin
# c = Celsius
while True:
    print('=' * 50, 'CONVERSOR: CELSIUS PARA KELVIN ', '=' * 50)
    c = float(input('Informe a temperatura em Celsius:'))
    k = c + 273.15
    print(f'A temperatura {c}° Celsius é igual a {k:.2f}° Kelvin.  ')
"""
while True:
    c = float(input(f'Insira um número em celsius:'))
    k = c + 273.15
    print(f'O valor de {c} celsius é igual a {k:.4} kevins.')

