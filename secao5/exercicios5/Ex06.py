"""
while True:
num1 = int(input('Informe o 1° número:'))
num2 = int(input('Informe o 2° número:'))
    if num1 > num2:
        print(f'O maior número é {num1}!')
        print(f'A diferença entre {num1} e {num2} é {num1 - num2}!')
    else: num2 > num1:
        print(f'O maior número é {num2}!')
        print(f'A diferença entre {num2} e {num1} é {num2 - num1}!')

lista = []
while True:
    for i in range(1, 3):
        num = float(input(f'Insira o {i}º número:'))
        lista.append(num)
        print(max(lista) é o maior número e )
"""

while True:
    print('%' * 150)
    num1 = int(input('Insira o 1º número inteiro:'))
    num2 = int(input('Insira o 2º número inteiro:'))
    if num1 < 0 or num2 < 0:
        print('Favor inserir número positivo e inteiro:')
    elif num1 > num2:
        print(f'{num1} é o maior dos números; {num1 - num2} é a diferença entre os dois números.')
    else:
        print(f'{num2} é o maior dos números; {num2 - num1} é a diferença entre os dois números.')
