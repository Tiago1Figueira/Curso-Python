"""
while True:
    print('='*50, 'CALCULO DE PREÇO', '=' *50)
    preco = float(input('Informe o preço do produto:'))
    if preco < 50:
        preco_aumentado = preco + (preco * 0.05)
    elif preco > 50 or preco < 100:
        preco_aumentado = preco + (preco * 0.10)
    else:
        preco_aumentado = preco + (preco * 0.15)

    if preco_aumentado < 80:
        print(f'O preço {preco_aumentado:.2f} é barato!')
    elif 80 <= preco_aumentado >= 120:
        print(f'O preço {preco_aumentado:.2f} é normal!')
    elif 120 < preco_aumentado >= 200:
        print(f'O preço {preco_aumentado:.2f} é caro!')
    else:
        print(f'O preço {preco_aumentado:.2f} é muito caro!')
"""
while True:
    print('%' * 150)
    preco = float(input('Informe o preço do produto:'))
    if preco <= 50:
        valor = preco + (preco * 0.05)
    elif preco > 50 and preco <= 100:
        valor = preco + (preco * 0.10)
    else:
        valor = preco + (preco * 0.15)

    if valor <= 80:
        print(f'{valor} Barato!')
    elif valor > 80 and valor <= 120:
        print(f'{valor} Normal!')
    elif valor > 120 and valor <= 200:
        print(f'{valor} Caro!')
    else:
        print(f'{valor} Muito caro!')
