"""
#1
from time import sleep
n = int(input('Informe um número:'))
for i in range(0, n + 1):
    sleep(0.2)
    print(i, end= ' ')

#2
from time import sleep
num = int(input('Informe um número inteiro e positivo:'))
while num < 0:
    print('Atenção: o número deve ser inteiro e positivo! ')
    num = int(input('Informe um número inteiro e positivo:'))
for i in range(0, num + 1):
    sleep(0.2)
    print(i, end=' ')

#3
while True:
    num = float(input('\nInforme um número:'))
    while num != int(num):
        print('Número inválido!')
        num = float(input('\nInforme um número:'))
    for i in range(0, int(num) + 1):
        print(i,end=' ')

while True:
    print('%' * 50, 'IMPRIMA TODOS OS VALORES DE 0 ATÉ O NÚMERO INSERIDO PELO USUÁRIO:', '%' * 50)
    num = float(input('Insira um número inteiro e positivo:'))
    while num < 0 or num != int(num):
        print('Número inválido!')
        num = float(input('Insira um número inteiro e positivo:'))
    for i in range(0, int(num)):
        print(i, end=' ')
    print('\n')
"""
while True:
    print('%' * 50, 'IMPRIMA TODOS OS VALORES DE 0 ATÉ O NÚMERO INSERIDO PELO USUÁRIO:', '%' * 50)
    num = float(input('Insira um número inteiro e positivo:'))
    while num != int(num) or num <= 0:
        print('Favor informar número inteiro e positivo!')
        num = float(input('Insira um número inteiro e positivo:'))
    for i in range(0, int(num) + 1):
        print(i, end=' ')
    print('/n')
