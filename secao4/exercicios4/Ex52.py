"""
ap1 = 0.46
ap2 = 0.37
ap3 = 0.17
premio = float(input('Informe o valor do prêmio:'))
apostador1 = premio * ap1
apostador2 = premio * ap2
apostador3 = premio * ap3
print(f'Prêmio apostador 1 = {apostador1:.2f}\nPrêmio apostador 2 = {apostador2:.2f}\nPrêmio apostador 3 =
{apostador3:.2f}')
"""

variavel = 100
while True:
    aposta1 = float(input('Insira o valor apostado pelo 1º apostador:'))
    aposta2 = float(input('Insira o valor apostado pelo 2º apostador:'))
    aposta3 = float(input('Insira o valor apostado pelo 3º apostador:'))
    premio = float(input('Insira o valor do prêmio:'))
    valor1 = (aposta1 / premio)
    valor2 = (aposta2 / premio)
    valor3 = (aposta3 / premio)
    premio1 = valor1 * premio
    premio2 = valor2 * premio
    premio3 = valor3 * premio
    print(f'Prêmio proporcional: Apostador 1 {premio1} reais, Apostador 2 {premio2} reais,'
          f' Apostador 3 {premio3} reais.')
