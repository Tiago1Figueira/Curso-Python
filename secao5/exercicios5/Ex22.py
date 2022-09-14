"""
# 1
while True:
    print('=' * 50, 'CÁLCULO PARA A APOSENTADORIA', '=' * 50)
    idade = int(input('Informe a sua idade:'))
    tempo_servico = float(input('Informe o seu tempo de serviço:'))
    if idade >= 65 or tempo_servico >= 30 or idade >= 60 and tempo_servico >= 25:
        print('Pode se aposentar!')
    else:
        print('Não pode se aposentar!')
# 2
while True:
    print('=' * 50, 'CÁLCULO PARA A APOSENTADORIA', '=' * 50)
    idade = int(input('Informe a sua idade:'))
    tempo_servico = float(input('Informe o seu tempo de serviço:'))
    if idade >= 65:
        print('Pode se aposentar!')
    if tempo_servico >= 30:
        print('Pode se aposentar!')
    if idade >= 60 and tempo_servico >= 25:
        print('Pode se aposentar!')
    else:
        print('Não pode se aposentar!')
"""

while True:
    print('%' * 50, 'PODE APOSENTAR?', '%' * 85)
    idade = int(input('Informe a sua idade:'))
    tempo_trabalhado = int(input('Informe o tempo de serviço:'))
    if idade >= 65:
        print('Pode aposentar!')
    elif tempo_trabalhado >= 30:
        print('Pode aposentar!')
    elif idade >= 60 and tempo_trabalhado >= 25:
        print('Pode aposentar!')
    else:
        print('Não pode aposentar!')