"""
soma = 0
for i in range(1,4):
    num = int(input(f'Informe o {i}° número inteiro:'))
    soma += num
print(f'A soma dos números é igual a {soma}!')

soma = 0
for i in range(1, 4):
    num = int(input(f'Informe o {i}º número inteiro:'))
    soma += num
print(f'A soma dos números é igual a {soma}!')

soma = 0
for i in range(1, 4):
    num = int(input(f'Informe o {i}º número inteiro:'))
    soma += num
print(f'A soma dos números é igual a {soma}!')
"""
while True:
    soma = 0
    for i in range(1, 4):
        num = int(input(f'Informe o {i}º número:'))
        soma += num
    print(f'A soma dos números é {soma}')
