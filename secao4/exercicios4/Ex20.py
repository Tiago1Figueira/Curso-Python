"""
# k = quilogramas e l = libras
while True:
    k = float(input('Informe a quantidade de quilos:'))
    l = k / 0.45
    print(f'{k} quilos são iguais a {l:.2f} libras!')
"""

while True:
    print('%'*50, 'Conversor: quilos para libras','%'*50)
    k = float(input(f'Insira o valor em quilos:'))
    l = k / 0.45
    print(f'{k} quilos são iguais a {l:.5} libras.')
