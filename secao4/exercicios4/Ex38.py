"""
aumento = 0.25
while True:
    print('=' * 50, 'CALCULE VALOR DO SALÁRIO:', '=' * 50)
    sal = float(input('Informe um salário:'))
    sal_aumento = sal + (sal * aumento)
    print(f'O salário com 25% de aumento é {sal_aumento} reais!')
"""
aumento = 0.25
while True:
    print('%' * 50, 'SALÁRIO CORRIGIDO', '%' * 50)
    salario = float(input('Insira o valor do salário:'))
    salario_aumentado = salario + (salario * aumento)
    print(f'O valor do salário corrigido é {salario_aumentado:.2f} reais.')

