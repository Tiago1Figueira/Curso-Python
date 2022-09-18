"""
#1
soma = 0
for num in range(0,10):
    num = int(input('Informe um número: '))
    soma += num
print(soma)

#2
soma = 0
for i in range(1, 11):
    num = int(input(f'Informe o {i}° número:'))
    soma = soma + num
print(soma)

#3
soma = 0
for i in range(1,11):
    valores = float(input(f'Informe {i}° valor:'))
    soma += valores
print(soma)
"""
while True:
    print("%" * 50, 'CALCULA A SOMA DE 10 NÚMEROS REAIS!', "%" * 50)
    soma = 0
    for i in range(1, 11):
        num = float(input(f'Informe o {i}º número:'))
        soma += num
    print(f'A soma dos 10 números é {soma}!')
