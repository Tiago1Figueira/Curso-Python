"""
#1
num = int(input('Informe um número:'))
for num in range(1, num+num):
    if num % 2 != 0:
        impares = num
        print(impares, end=' ')

#2
impares = 0
num = int(input('Informe um número inteiro:'))
for i in range(0, num + 1):
    if i % 2 != 0:
        impares = i
        print(impares, end=' ')

#3
impares = 0
num = float(input('Informe um número inteiro:'))
while num != int(num):
    print('Número inválido!')
    num = float(input('Informe um número inteiro:'))
    for i in range(0, int(num) + 1):
        if i % 2 != 0:
            impares = i
            print(impares,end=' ')

while True:
    print('%' * 50, 'ACHA VALORES ÍMPARES DENTRO DE UMA SEQUÊNCIA LIMITADA DE NÚMEROS:', '%' * 50)
    num = float(input('Informe um número natural inteiro:'))
    while num != int(num):
        print('Não é número natural inteiro:')
        num = float(input('Informe um número natural inteiro:'))
    for i in range(0, int(num)):
        if i % 2 != 0:
            print(f'{i}', end=' ')
    print('\n')

"""
while True:
    print('$' * 50, 'Encontra os números ímpares antes de um número natural lido:', '$' * 50)
    num = float(input(f'Insira um número inteiro:'))
    while num != int(num):
        print('Favor informar número inteiro!')
        num = float(input(f'Insira um número inteiro:'))
    for i in range(1, int(num) + 1):
        if i % 2 != 0:
            print(i, end=' ')
    print('/n')











