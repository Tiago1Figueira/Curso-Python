"""
valor_hora = 30
ir = 0.08
while True:
    print('=' * 150)
    dias = float(input('Informe quantos dias foram trabalhados:'))
    salario = (dias * valor_hora)
    salario_desc = salario - (salario * ir)
    print(f'O valor do salário descontado do I.R. é {salario_desc:.2f}!')
"""
desconto = 0.08
valor_hora = 30
while True:
    print('%' * 50, 'Salário do Encanador', '%' * 50)
    dias = float(input('Insira o número de dias trabalhados:'))
    salario = (valor_hora * dias)
    salario_descontado = salario - (salario * desconto)
    print(f'O valor a pagar para o encanador será {salario_descontado:.2f} reais.')
