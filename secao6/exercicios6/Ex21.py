"""
#1
soma = 0
multiplicacao = 1
num1 = int(input('Informe o 1° número:'))
num2 = int(input('Informe o 2° número:'))
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        soma += i
    if i % 2 != 0:
        multiplicacao *= i
print(f"A soma dos números pares é {soma} e a multiplicação dos ímpares é {multiplicacao}.")

#2
print('='* 55, 'SOMA DE PARES E MULTIPLICAÇÃO DE ÍMPARES DE UM INTERVALO:', '='*55)
multiplicacao_impares = 1
soma_pares = 0
num1 = int(input('Informe o primeiro número:'))
num2 = int(input('Informe o segundo número:'))
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        soma_pares += i
    elif i % 2 != 0:
        multiplicacao_impares *= i
print(f'A soma é {soma_pares}.\n')
print(f'Multiplicação {multiplicacao_impares}.\n')
print('='*175)

#3
soma = 0
multiplicacao = 1
while True:
    print('='*80)
    num1 = int(input('Informe o primeiro número:'))
    num2 = int(input('Informe o segundo número:'))
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            soma += i
        elif i % 2 != 0:
            multiplicacao *= i
    print(f'A soma dos números pares no intervalo {num1} e {num2} é {soma}.')
    print(f'A multiplicação dos números ímpares no íntervalo {num1} e {num2} é {multiplicacao} ')
"""
soma = 0
multiplica = 1
while True:
    print('%' * 50, 'RECEBE 2 NÚMEROS E GERA UM INTERVALO NUMÉRICO ENTRE ELES; SOMA OS PARES E MULTIPLICA OS ÍMPARES:',
          '%' * 50)
    num1 = float(input('Informe o 1º número inteiro:'))
    while num1 != int(num1):
        print('Número 1 inválido!')
        num1 = float(input('Informe o 1º número inteiro:'))
    num2 = float(input('Informe o 2º número inteiro:'))
    while num2 != int(num2):
        print('Número 2 inválido!')
        num2 = float(input('Informe o 2º número inteiro:'))

    for i in range(int(num1) - 1, int(num2) + 1):
        if i % 2 == 0:
            soma += i
        else:
            multiplica = multiplica * i
    print(f'{soma} é o valor da soma dos números pares do intervalo entre {num1} e {num2}.\n '
          f'{multiplica} é referente a multiplicação dos ímpares do intervalo {num1} e {num2}.')
    break # break o while True: mas elimina o acumulo de resultado de cálculos passados.(sem função clear.lista)

