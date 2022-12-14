"""
while True:
    num1 = int(input('Informe o 1° número:'))
    num2 = int(input('Informe o 2° número:'))
    if num1 > num2:
        print(f'O número {num1} é o maior!')
    elif num1 < num2:
        print(f'O número {num2} é o maior!')
    else:
        print(f'O números {num1} e {num2} são iguais!')
"""

while True:
    print('%' * 150)
    num1 = float(input(f'Insira o 1º número:'))
    num2 = float(input(f'Insira o 2º número:'))
    if num1 == num2:
        print(f'{num1} é igual a {num2}.')
    elif num1 > num2:
        print(f'{num1} é o maior número.')
    else:
        print(f'{num2} é o maior número.')
