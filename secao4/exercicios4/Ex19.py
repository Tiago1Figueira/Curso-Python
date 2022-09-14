"""
#2
from python_total.curso_python.secao4.exercicios4.Ex18 import m

print(m)

#1
# m = metros cúbicos e l = litros
while True:
    print('=' * 50, 'CONVERSOR: LITROS PARA METROS CÚBICOS!', '=' * 50)
    l = float(input('Informe a quantidade de litros:'))
    m =  l / 1000
    print(f'O valor de {l} litros é igual a {m} metros cúbicos!')

"""
while True:
    print('%'*50, 'Conversor: litros para metros cúbicos','%'*50)
    l = float(input('Insira o valor em litros:'))
    m =  l / 1000
    print(f'{l} litros são iguais a {m} metros cúbicos.')
