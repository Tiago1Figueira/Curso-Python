"""
while True:
    print('=' * 50, 'CÁLCULO DOS 20% DO EMPRÉSTIMO:', '=' * 50)
    sal = float(input('Informe o valor do salário:'))
    prestacao = float(input('Informe o valor da prestação:'))
    if prestacao > sal * 20/100:
        print('Empréstimo não concedido!')
    else:
        print('Empréstimo concedido!')
"""
while True:
    print('%' * 150)
    salario = float(input('Informe o salário:'))
    prestacao = float(input('Informe o valor da prestação:'))
    if prestacao > (salario * 0.20):
        print(f'Empréstimo não concedido!')
    else:
        print(f'Empréstimo concedido!')
