"""
# m = metros quadrados and h = hectares
while True:
    print('=' * 50 , 'CONVERSOR: METROS QUADRADOS PARA HECTARES', '=' * 50)
    m = float(input('Informe o valor em metros:'))
    h = m * 0.0001
    print(f'{m} metros quadrados são iguais a {h} hectares.')
"""
while True:
    print('%' * 50, 'CONVERSOR: METROS QUADRADOS EM HECTARES', '%' * 50)
    m = float(input('Insira um número em metros quadrados:'))
    h = m * 0.0001
    print(f'{m} metros quadrados são iguais a {h:.2} hectares.')
