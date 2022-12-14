"""
#1
soma = 0
media = 0
for num in range(0, 10):
    num = int(input('Informe um número:'))
    while num < 0:
       print('Atenção: número deve ser positivo!')
       num = int(input('Informe um número:'))
    soma += num
    media = soma / 10
print(f'A média dos números digitados é {media}')

#2
soma = 0
cont = 0
for i in range(1, 11):
    num = int(input(f'Informe o {i}° número:'))
    while num < 0:
        print('Atenção: o número dever ser positivo!')
        num = int(input(f'Informe o {i}° número:'))
cont += 1
soma += num
media = soma / cont
print(f'O valor da média é {media}.')

#3
media = 0
soma = 0
cont = 0
for i in range(1,11):
    numero = float(input(f'Informe o {i}° número: '))
    while numero < 0 :
        print('Atenção: o número deve ser maior que 0!')
        numero = float(input(f'Informe o {i}° número: '))
    soma += numero
    cont += 1
    media = soma / cont
print(f'O valor da média dos números dados é {media}!')
"""
soma = 0
while True:
    print("%" * 50, 'CÁLCULO DA MÉDIA DE 10 NÚMEROS INTEIROS POSITIVOS IGNORANDO OS NEGATIVOS:', '%' * 50)
    for i in range(1, 11):
        num = float(input(f'Insira o {i}º número inteiro e positivo:'))
        while num < 0 or num == float:
            print('Número inválido!')
            num = float(input(f'Insira o {i}º número inteiro e positivo:'))
        soma += num
        media = soma / 10
    print(f'A a média dos 10 número inteiros e positivos será {media}!')

