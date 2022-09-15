"""
#imc = indice de massa corporal
while True:
    print('='*150)
    peso = float(input('Informe o seu peso:'))
    altura = float(input('Informe a sua altura:'))
    imc = peso / (altura)**2
    if imc < 18.5:
        print(f'I.M.C = {imc:.2f} Abaixo do peso!')
    elif imc >= 18.5 and imc <= 24.9:
        print(f'I.M.C. = {imc:.2f} Saudável!')
    elif imc >= 25 and imc <= 29.9:
        print(f'I.M.C = {imc:.2f} Peso em excesso!')
    elif imc >= 30 and imc <= 34.9:
        print(f'I.M.C = {imc:.2f} Obesidade grau I!')
    elif imc >= 35 and imc <= 39.9:
        print(f'I.M.C = {imc:.2f} Obesidade grau II(severa)!')
    else:
        print(f'I.M.C = {imc:.2f} Obesidade grau III(mórbida)!')
"""

while True:
    print("%" * 50, "CALCULADOR DE MASSA CORPORAL", "%" * 70)
    peso = float(input('Informe o seu peso:'))
    altura = float(input('Informe a sua altura:'))
    imc = peso / (altura) ** 2
    if imc <= 18.5:
        print('Abaixo do peso!')
    elif imc >= 18.6 and imc <= 24.9:
        print('Saudável')
    elif imc >= 25 and imc <= 29.9:
        print('Peso em excesso!')
    elif imc >= 30 and imc <= 34.9:
        print('Obesidade Grau 1!')
    elif imc >= 35 and imc <= 39.9:
        print('Obesidade Severa (Grau 2)!')
    elif imc >= 40:
        print('Obesidade Morbida (Grau 3)!')
    else:
        print('Favor digitar valor válido!')



