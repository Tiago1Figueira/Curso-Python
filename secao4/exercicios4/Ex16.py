"""
# p = polegadas e c = centímetros
while True:
    print('=' * 50,'CONVERSOR: POLEGADAS PARA CENTÍMETROS', '=' * 50)
    p = float(input('Informe o valor em polegadas:'))
    c = p * 2.54

    print(f'O valor de {p} polegadas é igual a {c:.2f} centímetros!')
"""

while True:
    print('%'*50, 'Conversor polegadas para centímetros', '%'*50)
    p = float(input(f'Insira a quantidade de polegadas:'))
    c = p * 2.54
    print(f'{p} polegadas são iguais a {c:.4} centímetros. ')
