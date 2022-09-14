"""
cotacao = 5.4
while True:
    print('=' * 50, "CONVERSOR REAL - DÓLAR")
    real = float(input('Informe a quantia em real para obter quantia em dólares:'))
    dolar = real / cotacao
    print(f'A cotação de ${real} reais para dólares é ${dolar:.2f} dólares!')
"""
while True:
    print('=' * 50, "CONVERSOR REAL - DÓLAR", '=' * 50)
    real = float(input('Insira o valor em reais:'))
    dolar = real / 5.75
    print(f'{real} reais são iguais a {dolar:.3} dólares.') # :.3f - "f" significa qtas casas após a vírgula.
