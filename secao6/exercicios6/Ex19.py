"""
#1
num = input('Informe um número entre 100 e 999:')
for n in num:
    print(n, end=' ')

#2
num = input('Informe um número entre 100 a 999:')
for i in num:
    print(i, end=' ')

#4
#3
while True:
    num = float(input('\nInforme um número inteiro entre 100 e 999:'))
    while num < 100 or num > 999 or num != int(num):
        print('Número inválido!')
        num = float(input('\nInforme um número inteiro entre 100 e 999:'))
    for i in str(num):
        print(i)

#checar pq o a casa decimal está aparecendo no print.
"""
while True:
    print('%' * 50, 'IMPRIMIR CADA ALGARISMO DE UM NÚMERO INSERIDO PELO USUÁRIO ENTRE 100 E 999', '%' * 50)
    num = input('Inserir um número entre 100 e 999:')
    while num < str(100) or num > str(999):
        print('Número Inválido!')
        num = input('Inserir um número entre 100 e 999:')
    string = str(num)
    # pode ser feito assim:

    # for i in num:
    #     print(i)

    # ou pode ser feito assim:
    print(num[0])
    print(num[1])
    print(num[2])
