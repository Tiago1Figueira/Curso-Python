"""
#1
soma = 0
for num in range(0,10):
    num = int(input('Informe um número:'))
    soma += num
    media = soma / 10
print(f'A média dos números digitados é {media}')

#2
soma = 0
cont = 0
for i in range(1,11):
    num = int(input(f'Informe o {i}° número:'))
    soma += num
    cont += 1
    media = soma / cont
print(f'A média dos números digitados é {media}!')

#3
media = 0
soma = 0
cont = 0
for i in range(1,11):
    numero = int(input(f'Informe o {i}° número inteiro:'))
    soma += numero
    cont = cont + 1
    media = soma / cont
print(f'A média dos números informados é {media}!')

#4
lista = [ ]
for i in range(1,11):
    numero = int(input(f'Informe o {i}° número inteiro:'))
    lista.append(i)
print(f'A média dos números informados é {sum(lista) / len(lista)}!')


soma = 0
cont = 0
while True:
    print('%' * 50, 'CÁLCULO DE MÉDIA DE 10 NÚMEROS INTEIROS:', '%' * 50)
    for i in range(1, 11):
        num = int(input(f'Insira o {i}º número inteiro:'))
        soma += num
        cont += 1
        media = soma / cont
    print(f'O valor da média é {media}!')
"""
soma = 0
cont = 0
media = " "
while True:
    print('%' * 50, 'Calcula o valor da média de 10 números inteiros', '%' * 50)
    for i in range(1, 11):
        num = float(input(f'Informe o {i}º número inteiro:'))
        while num != int(num):
            print('Favor informar número inteiro!')
            num = float(input(f'Informe o {i}º número inteiro:'))
        soma = soma + num
        cont = cont + 1
        media = soma / cont
    print(f'O valor da média dos números é {media}.')
