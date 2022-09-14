"""
while True:
    print("=" * 50, 'CALCULE A OPERAÇÃO', "=" * 50)
    num = int(input('Informe um número inteiro:'))
    soma = ((num * 3) + 1) + ((num * 2) - 1)
    print(f'A soma é {soma}!')

"""

while True:
    print("%" * 50, 'CALCULE A OPERAÇÃO', "%" * 50)
    num = int(input('Insira um número inteiro:'))
    triplo = (num * 3) + 1
    dobro = (num * 2) - 1
    soma = triplo + dobro
    print(f'A soma do sucessor do triplo do número {num} com o antecessor do seu dobro é {soma}.')
