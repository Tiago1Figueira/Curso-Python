"""
#1
# o programa está cobrando mais horas do que deveria. Acrescenta 40 min a mais em cada hora!
#horario_chegada = hc e horário partida = hp
while True:
    print('=' * 150)
    hc = int(input('Informe horário de chegada(HHMM):'))
    while hc % 2 != 0 or hc != int(hc):
        print('O horário de chegada deve ser arredondado e par!')
        hc = int(input('Informe horário de chegada(HHMM):'))
    hp = int(input('Informe horário de partida(HHMM):'))
    while hp % 2 != 0 or hp != int(hp):
        print('O horário de partida deve ser arredondado e par!')
        hp = int(input('Informe horário de partida(HHMM):'))
    qtd = hp/60 - hc/60
    if qtd <= 1:
        print(f'Pagar 1 reais por 1 hora!')
    elif qtd > 1 and qtd <= 2:
        print(f'Pagar 2 reais por 2 horas!')
    elif qtd > 2 and qtd <= 3:
        print(f'Pagar 3.40 reais por 3 horas!')
    elif qtd > 3 and qtd <= 4:
        print(f'Pagar 4.80 reais por 4 horas!')
    elif qtd > 4 and qtd <= 5:
        print(f'Pagar 6.80 reais por 5 horas')
    elif qtd > 5:
        pagar = (((qtd) - 5) * 2) + 6.80
        print(f'Pagar {pagar:.1f} reais pro {qtd/60:.1f} horas!')
    elif qtd >= 1440:
        pagar = (((qtd) - 24 )* 1) + 50
        print(f'Pagar {pagar:.1f} reais pela diária e horas extras!')

    print(f'{qtd:.1f} horas')

#2
while True:
    print('%' * 50, 'CÁLCULO DE VALOR A PAGAR EM ESTACIONAMENTO:', "%" * 50)
    hc = int(input('Informe a hora de chegada:'))
    while hc < 0 or hc >= 25:
        print('Hora inválida!')
        hc = int(input('Informe a hora de chegada:'))
    mc = int(input('Informe os minutos de chegada:'))
    while mc < 0 or mc >= 60:
        print('Minutos inválidos!')
        mc = int(input('Informe os minutos de chegada:'))
    hs = int(input('Informe a hora de saída:'))
    while hs < 0 or hs >= 25:
        print('Hora inválida!')
        hs = int(input('Informe a hora de saída:'))
    ms = int(input('Informe os minutos de saída:'))
    while ms < 0 or ms >= 60:
        print('Minutos inválidos!')
        ms = int(input('Informe os minutos de saída:'))
    qtd = (hc + mc) / 60
"""
