"""
#1
soma = 0
num = int(input('Informe um número inteiro positivo: '))
while num <=0:
    num = int(input('Informe um número inteiro positivo: '))
for i in range(0, num + 1):
    soma += i
print(f'A soma de todos os números de 0 a {num} é {soma} !')

#2
soma = 0
num = int(input('Informe um número inteiro e positivo:'))
while num < 0:
    print('Atenção: digite número inteiro e positivo!')
    num = int(input('Informe um número inteiro e positivo:'))
for i in range(0, num + 1):
    soma += i
    print(soma, end=' ')

#3
soma = 0
while True:
    num = float(input('Informe um número inteiro e positivo:'))
    while num < 0 or num != int(num):
        print('Número inválido!')
        num = float(input('Informe um número inteiro e positivo:'))
    for i in range(0, int(num) + 1):
        soma = soma + i
    print(soma)

#4
lista = []
while True:
    num = float(input('Informe um número inteiro e positivo:'))
    while num <= 0 or num != int(num):
        print('Número inválido!')
        num = float(input('Informe um número inteiro e positivo:'))
    for i in range(1, int(num) + 1):
        lista.append(i)
    print(sum(lista))
    lista.clear()

soma = 0
while True:
    print('%' * 50, 'SOMA TODOS OS NÚMEROS INTEIROS POSITIVOS DE 0 ATÉ O NÚMERO INSERIDO PELO USUÁRIO:','%' * 50)
    num = float(input('Insira um número inteiro e positivo:'))
    while num < 0 or num != int(num):
        print('Número inválido!')
        num = float(input('Insira um número inteiro e positivo:'))
    for i in range(0, int(num + 1)):
        soma += i
    print(f'O valor da soma dos números de 0 até {num} é igual a {soma}!')
    break #colocado pra evitar a soma constante de vários lançamentos!Contudo, quebra o while true:!

"""
soma = 0
while True:
    print('%' * 50, 'SOMA TODOS OS NÚMEROS INTEIROS POSITIVOS '
                    'DE 0 ATÉ O NÚMERO INSERIDO PELO USUÁRIO:', '%' * 50)
    num = float(input('Insira um número inteiro e positivo:'))
    while num != int(num) or num < 0:
        print('Número inválido!')
        num = float(input('Insira um número inteiro e positivo:'))
    for i in range(0, int(num) + 1):
        soma = soma + i
        print(i, end=' ')
    print('/n')
    print(f'A soma dos números acime é {soma}!')
    break  # colocado pra evitar a soma constante de vários lançamentos!
           # Contudo, quebra o while true:!
