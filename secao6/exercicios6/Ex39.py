"""
#1
print('=' *60, 'Cálculo da áre de um triângulo', '='*60)
base = float(input('Informe o valor da base:'))
altura = float(input('Informe o valor da altura:'))
while base <= 0 or altura <= 0:
    print('Atenção: informe números maiores que 0!')
    base = int(input('Informe o valor da base:'))
    altura = int(input('Informe o valor da altura:'))
area_triangulo = base * altura / 2
print(f'A área do triângulo é {area_triangulo:.2f}!!')
print('=' * 175)

#2
altura = float(input('Informe a altura do triângulo:'))
base = float(input('Informe a base do triângulo:'))
while altura <= 0 or base <= 0:
    print('=' * 155)
    print('Atenção: digite valores positivos e diferentes de 0 para altura e base do triângulo!!')
    altura = float(input('Informe a altura do triângulo:'))
    base = float(input('Informe a base do triângulo:'))
area_triangulo = (base * altura) / 2
print(f'A área do triângulo de base {base} e de altura {altura} é {area_triangulo}!!')


#3
while True:
    print('='*80)
    base = float(input('Informe a altura do triângulo:'))
    while base <= 0:
        print('Atenção: o número deve ser maior que zero!')
        base = float(input('Informe a altura do triângulo:'))
    altura = float(input('Informe a base do triângulo:'))
    while altura <= 0:
        print('Atenção: o número deve ser maior que zero!')
        altura = float(input('Informe a base do triângulo:'))
    area_triangulo = base * altura / 2
    print(f'A área do triângulo é {area_triangulo:.2f}')
"""
while True:
    print('#' * 100)
    base = float(input('Insira o valor da base do triângulo:'))
    altura = float(input('Insira o valor da altura do triângulo:'))
    if base <= 0 or altura <= 0:
        print('Valores nulos ou negativos! Tente novamente!')
    else:
        area = (base * altura) / 2
        print(f'Área do triângulo = {area:.2f}')
