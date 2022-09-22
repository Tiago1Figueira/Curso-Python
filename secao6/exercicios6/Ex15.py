"""
#1
num = int(input('Informe um número positivo ímpar:'))
while num % 2 == 0 or num < 0:
    num = int(input('Informe um número positivo ímpar:'))
for i in range(1, num + 1):
        if i % 2 !=0:
            print(i, end=' ')

#2
num = int(input('Informe um número inteiro, positivo e ímpar: '))
while num < 0:
    print('Atenção: digite número inteiro, positivo e ímpar:')
    num = int(input('Informe um número inteiro, positivo e ímpar: '))
for i in range(1, num + 1):
    if i % 2 != 0:
        print(i, end='  ')
#3
while True:
    num = float(input('\nInforme um número inteiro ímpar:'))
    while num % 2 == 0 or num < 0 or num != int(num):
        print('Número inválido!')
        num = float(input('\nInforme um número inteiro ímpar:'))
    for i in range(1, int(num + 1)):
        print(i, end=' ')
"""
while True:
    print('%' * 50, 'IMPRIMIR TODOS OS NÚMERO ÍMPARES DE 1 ATÉ O NÚMERO INSERIDO PELO USUÁRIO', '%' * 50)
    num = float(input('Insira um número inteiro positivo e ímpar:'))
    while num < 0 or num != int(num) or num % 2 == 0:
        print('Número inválido!')
        num = float(input('Insira um número inteiro positivo e ímpar:'))
    for i in range(1, int(num + 1)):
        if i % 2 != 0:
            print(i, end=' ')
    print('\n')
