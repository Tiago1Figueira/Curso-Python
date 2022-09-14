"""
lista = [ ]
for i in range(1,3):
    num = int(input(f'Informe o {i}° número:'))
    lista.append(num)
print(f'O maior número é o {max(lista)}')

lista = []
while True:
    for i in range(1, 3):
        num = float(input(f'Insira o {i}º número:'))
        lista.append(num)
    print(f'O maior número entre os dois é {max(lista)}.')
"""
while True:
    print('%' * 150)
    num1 = float(input('Insira o primeiro número:'))
    num2 = float(input('Insira o segundo número:'))
    if num1 > num2:
        print(f'O maior número é {num1}.')
    else:
        print(f'O maior número é {num2}.')

