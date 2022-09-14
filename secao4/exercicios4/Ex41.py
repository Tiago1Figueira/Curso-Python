"""
while True:
    print('=' * 150)
    valor_hora = float(input('Informe o valor a ser pago por hora:'))
    horas = int(input('Informe o número de horas trabalhadas:'))
    salario = valor_hora * horas
    salario_final = salario + (salario * 0.10)
    print(f'O valor do seu salário salário final é {salario_final:.2f} !')
"""

percentual_aumento = 0.10
while True:
    print('%' * 150)
    horas = float(input('Insira o valor da hora trabalhada:'))
    qtas_horas = float(input('Insira a quantidade de horas trabalhadas:'))
    salario = horas * qtas_horas
    salario_adicionado = salario + (salario * percentual_aumento)
    print(f'O valor do salário do funcionário será {salario_adicionado:.2f} reais.')
