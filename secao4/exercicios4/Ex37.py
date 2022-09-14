"""
desconto = 0.12
while True:
    print('=' * 50, 'CALCULE VALOR PRODUTO COM DESCONTO:', '=' * 50)
    valor = float(input('Informe o valor do produto:'))
    valor_final = valor - (valor * desconto)
    print(f'O valor de produto já descontado é {valor_final:.2f}!')
"""
desconto = 0.12
while True:
    print('%' * 50, 'CÁLCULO DO VALOR DO PRODUTO COM DESCONTO:', '%' * 50)
    valor = float(input('Insira o valor do produto:'))
    valor_descontado = valor - (valor * desconto)
    print(f'O valor do produto com o desconto é de {valor_descontado:.2f}.')
