"""
bonus = 0
while True:
    print('=' * 150)
    sal = int(input('Informe o salário atual:'))
    temposer = int(input('Informe o tempo de serviço:'))
    if temposer < 1:
        bonus = 0
    elif temposer >= 1 and temposer <= 3:
        bonus = 100
    elif temposer >= 4 and temposer <= 6:
        bonus = 200
    elif temposer >= 7 and temposer <= 10:
        bonus = 300
    else:
        bonus = 500
    if sal > 2000 and temposer < 1:
        print('Sem bônus ou reajuste!')
    elif sal <= 500:
        sal = sal + (sal * 0.25) + bonus
    elif sal <= 1000:
        sal = sal + (sal * 0.20) + bonus
    elif sal <= 1500:
        sal = sal + (sal * 0.15) + bonus
    elif sal <= 2000:
        sal = sal + (sal * 0.10) + bonus
    else:
        sal = sal + (sal * 0.00) + bonus
    print(f'O seu salário ajustado é {sal}!')
"""
reajuste1 = 0.25
reajuste2 = 0.20
reajuste3 = 0.15
reajuste4 = 0.10
reajuste5 = 0.00
while True:
    print('%' * 50, 'CALCULADOR DE SALÁRIO COM BÔNUS E REAJUSTE:', '%' * 50)
    tempo_servico = int(input('Insira o tempo de serviço em anos:'))
    if tempo_servico <= 1:
        bonus = 000
    elif tempo_servico > 1 and tempo_servico <= 3:
        bonus = 100
    elif tempo_servico > 3 and tempo_servico <= 6:
        bonus = 200
    elif tempo_servico > 6 and tempo_servico <= 10:
        bonus = 300
    else:
        bonus = 500
    sal_atual = float(input('Insira o salário atual:'))
    while sal_atual <= 0:
        print('Salário incorreto!')
        sal_atual = float(input('Insira o salário atual:'))
    if sal_atual <= 500:
        sal_aumentado1 = sal_atual + (sal_atual * reajuste1) + bonus
        print(f'Seu salário atualizado será {sal_aumentado1:.2f} reais.')
    elif sal_atual > 500 and sal_atual <= 1000:
        sal_aumentado2 = sal_atual + (sal_atual * reajuste2) + bonus
        print(f'Seu salário atualizado será {sal_aumentado2:.2f} reais.')
    elif sal_atual > 1000 and sal_atual <= 1500:
        sal_aumentado3 = sal_atual + (sal_atual * reajuste3) + bonus
        print(f'Seu salário atualizado será {sal_aumentado3:.2f} reais.')
    elif sal_atual > 1500 and sal_atual <= 2000:
        sal_aumentado4 = sal_atual + (sal_atual * reajuste4) + bonus
        print(f'Seu salário atualizado será {sal_aumentado4:.2f} reais.')
    else:
        sal_aumentado5 = sal_atual + (sal_atual * reajuste5) + bonus
        print(f'Seu salário atualizado será {sal_aumentado5:.2f} reais.')
