"""
#1
num = int(input('Informe um número inteiro e par:'))
while num <=0:
    num = int(input('Atenção: Informe um número inteiro e par:'))
    for i in range(num, -1, -1):
        print(i, end=' ')

#2
num = int(input('Informe um número inteiro, positivo e par:'))
while num < 0:
    num = int(input('Informe um número inteiro, positivo e par:'))
for i in range(num, -1, -1):
    if i % 2 == 0:
        print(i, end=' ')
#3
while True:
    num = float(input('\nInforme um número inteiro e par:'))
    while num % 2 != 0 or num != int(num):
        print('Número inválido!')
        num = float(input('\nInforme um número inteiro e par:'))
    for i in range(int(num), -1, -1):
        print(i, end=' ')
"""
while True:
    print('%' * 50, 'IMPRIMA TODOS OS VALORES PARES DE 0 ATÉ O NÚMERO INSERIDO PELO USUÁRIO NA ORDEM DECRESCENTE:',
          '%' * 50)
    num = float(input('Insira um número positivo e inteiro:'))
    while num < 0 or num != int(num):
        print('Número Inválido!')
        num = float(input('Insira um número positivo e inteiro:'))
    for i in range(int(num), -1, -1):
        if i % 2 == 0:
            print(i, end=' ')
    print('\n')
