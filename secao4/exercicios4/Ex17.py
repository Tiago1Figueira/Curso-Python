"""
# p = polegadas e c = centímetros
while True:
    print('=' * 50,'CONVERSOR: CENTÍMETROS PARA POLEGADAS', '=' * 50)
    c = float(input('Informe o valor em centímetros:'))
    p = c / 2.54

    print(f'O valor de {c} centímetros é igual a {p:.2f} polegadas!')
"""
while True:
    print('%'*50, 'Conversor: centímetros para polegadas', '%'*50)
    c = float(input(f'Insira o valor em centímetros:'))
    p = c / 2.54
    print(f'{c} centímetros são iguais a {p:.3} polegadas.')
