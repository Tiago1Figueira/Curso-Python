"""
while True:
    print('=' * 50, 'FÓRMULA PARA CÁLCULO DO TRAPÉZIO', '=' * 50)
    basemaior = float(input('Informe a base menor do trapézio:'))
    basemenor = float(input('Informe a base maior do trapézio:'))
    altura = float(input('Informe a altura do trapézio:'))
    trapezio = (basemaior + basemenor) * altura / 2
    print(f'A área do trapézio é {trapezio}!')
"""
while True:
    print('%' * 150)
    base_maior = float(input('Insira o valor da base maior do trapézio em cm :'))
    while base_maior <= 0:
        print('Valor inválido!')
        base_maior = float(input('Insira o valor da base maior do trapézio em cm:'))

    base_menor = float(input('Insira o valor da base menor do trapézio em cm:'))
    while base_menor <= 0:
        print('Valor inválido!')
        base_menor = float(input('Insira o valor da base menor do trapézio em cm:'))

    altura = float(input('Insira o valor da altura do trapézio em cm:'))
    while altura <= 0:
        print('Valor inválido!')
        altura = float(input('Insira o valor da altura do trapézio em cm:'))

    area = (base_maior + base_menor) * altura / 2
    print(f'A área do trapézio é {area:.2f} cm².')
