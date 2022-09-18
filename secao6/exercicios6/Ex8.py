"""
#1
lista = []
for num in range(0, 10):
    num = int(input('Informe um número:'))
    lista.append(num)
print(f'O maior número é {max(lista)} e o menor número é {min(lista)}')

#2
maior = -99999
menor = 99999
for i in range(0, 10):
    num = int(input('Informe um número:'))
    while num < 0:
        print(f'Atenção: o número deve ser positivo:')
        num = int(input('Informe um número:'))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f'O maior número é {maior} e o menor número é {menor}.')

#3
lista = []
for i in range(1, 11):
    num = float(input(f'Informe o {i}° número:'))
    while num < 0:
        print('Atenção: o número deve ser positivo:')
        num = float(input(f'Informe o {i}° número:'))
    lista.append(num)
print(f'Entre os números digitados o maior é {max(lista)} e o menor é {min(lista)}!!')

#4
lista = [ ]

for i in range(1,11):
    num = float(input(f'Informe o {i}° número'))
    while num < 0:
        print('Número inválido!')
        num = float(input(f'Informe o {i}° número'))
    lista.append(num)
print(f'O maior número da lista é {max(lista)} e o menor número é {min(lista)}!')

"""
maior = -9999999999
menor = 9999999999
while True:
    print('%' * 50, 'MOSTRAR O MAIOR E O MENOR NÚMERO DE UMA SEQUÊNCIA NUMÉRICA:', '%' * 50)
    for i in range(1, 11):
        num = float(input(f'Insira o {i}º número:'))
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    print(f'O maior número da sequência é {maior} e o menor é {menor}!')
