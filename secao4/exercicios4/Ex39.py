"""
porc1 = 0.46
porc2 = 0.32
porc3 = 0.22
while True:
    print('=' * 150)
    premio = float(input('Informe o valor do prêmio:'))
    a = premio * porc1
    print(f'O primeiro ganhador recebará {a:.2f}!')
    b = premio * porc2
    print(f'O segundo ganhador receberá {b:.2f}!')
    c = premio * porc3
    print(f'O terceiro ganhador receberá {c:.2f}!')
"""

while True:
    print('%' * 150, 'Valor do prêmio', '%' * 150)
    premio = float(input('Insira o valor do prêmio:'))
    ganhador1 = premio * 0.46
    ganhador2 = premio * 0.32
    ganhador3 = premio * 0.22
    print(f'{ganhador1:.2f} reais para o 1º colocado, {ganhador2:.2f} reais para o 2º e '
          f'{ganhador3:.2f} reais para o 3º colocado.')
