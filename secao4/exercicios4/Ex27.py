"""
# m = metros quadrados and h = hectares
while True:
    print('=' * 50, 'CONVERSOR: HECTARES PARA METROS QUADRADOS', '=' * 50)
    h = float(input('Informe o valor em hectares:'))
    m = h * 10000
    print(f' {h} hectares são iguais a {m} metros quadrados.')
"""
while True:
    h = float(input('Insira o valor em hectares:'))
    m = h * 10000
    print(f'{h} hectares são iguais a {m} metros quadrados.')
