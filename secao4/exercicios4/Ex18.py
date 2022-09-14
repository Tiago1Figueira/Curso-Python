"""
#2
from python_total.curso_python.secao4.exercicios4.Ex19 import l

print(l( ))

#1
# m = metros cúbicos e l = litros
while True:
    print('=' * 50, 'CONVERSOR: METROS CÚBICOS PARA LITROS!', '=' * 50)
    m = float(input('Informe quantos metros cúbicos quer converter:'))
    l = 1000 * m
    print(f'O valor de {m} metros cúbico é igual a {l} litros!')
"""
while True:
    print('%'*50, 'Conversor: metros cúbicos para litros', '%'*50)
    m = float(input(f'Insira o valor em metros cúbicos:'))
    l = 1000 * m
    print(f'{m} metros cúbicos são iguais a {l} litros.')




