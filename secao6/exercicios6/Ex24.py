"""
#1
soma = 0
num = int(input('Informe um número positivo:'))
while num <=0 :
    num = int(input('Informe um número positivo:'))
for i in range(1, num):
    if num % i == 0:
        soma += i
print(soma, end=' ')

#2
soma = 0
num = int(input('Informe um número inteiro e positivo:'))
while num <= 0:
    num = int(input('Informe um número inteiro e positivo:'))
for i in range(1, num +1):
    if num % i == 0:
        soma += i
print(soma)

#3
soma = []
while True:
    num = float(input('Informe um número inteiro e positivo:'))
    while num <=0 or num != int(num):
        print('Número inválido!')
        num = float(input('Informe um número inteiro e positivo:'))
    for i in range(1, int(num)):
        if num % i == 0:
            soma.append(i)
    print(f'A soma dos divisores do número {num} é {sum(soma)}!')
"""
soma = 0
while True:
    print('%' * 50, 'RECEBE UM NÚMERO E CALCULA A SOMA DE TODOS OS SEUS '
                    'DIVISORES EXCLUINDO ELE PRÓPRIO:', '%' * 50)
    num = float(input('Insira um número positivo e inteiro:'))
    while num <=0 or num != int(num):
        print('Número inválido!')
        num = float(input('Insira um número positivo e inteiro:'))
    for i in range(1, int(num)):
        if num % i == 0:
            soma += i
    print(f'A soma dos números divisores de {num} é {soma}.')
    # break = quebra o while true, mas tb não deixa que a soma seja um agregado das somas prévias.




















