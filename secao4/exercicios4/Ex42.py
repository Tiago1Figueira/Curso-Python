"""
grat = 0.05
imposto = 0.07
while True:
    print('=' * 150)
    salario_base = float(input('Informe o salário base:'))
    salario_liquido = salario_base - (salario_base * imposto)
    salario_receber = salario_liquido + (salario_liquido * grat)
    print(f'O seu salário será {salario_receber}!')
"""
gratificacao = 0.05
imposto = 0.07
while True:
    print('%' * 150)
    salario_base = float(input('Insira o salário base do funcionário:'))
    salario_base_com_gratificacao = salario_base + (salario_base * gratificacao)
    salario_liquido = salario_base_com_gratificacao - (salario_base_com_gratificacao * imposto)
    print(f'O salário líquido com a gratificação é {salario_base_com_gratificacao} reais.')
