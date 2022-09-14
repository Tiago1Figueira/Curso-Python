"""
desconto = 0.10
comissao = 0.05
while True:
    print('=' * 150)
    valor_produto = float(input('Informe o valor do produto:'))
    valor_descontado = valor_produto - (valor_produto * desconto)
    valor_parcela = valor_produto / 3
    valor_comissao_vista = valor_descontado * comissao
    valor_comissao_prazo = valor_produto * comissao
    print(f'Valor produto {valor_produto:.2f} reais.')
    print(f'Valor descontado {valor_descontado:.2f} reais.')
    print(f'Valor parcelado em 3 x sem juros {valor_parcela:.2f} reais.')
    print(f'Valor comissão - a vista {valor_comissao_vista:.2f} reais.')
    print(f'Valor comissão - a prazo {valor_comissao_prazo:.2f} reais. ')
"""
desconto = 0.10
comissao = 0.05
while True:
    print('%' * 150)
    valor = float(input('Insira o valor total:'))
    valor_a_vista = valor - (valor * desconto)
    valor_parcelado = valor / 3
    valor_comissao_vista = valor_a_vista * comissao
    valor_comissao_prazo = valor * comissao
    print(f'Valores: valor a vista {valor_a_vista:.2f} reais;'
          f'valor parcelado em 3x {valor_parcelado:.2f} reais;'
          f'valor comissão venda a vista {valor_comissao_vista:.2f} reais;'
          f'valor comissão venda a prazo {valor_comissao_prazo:.2f} reais;')
