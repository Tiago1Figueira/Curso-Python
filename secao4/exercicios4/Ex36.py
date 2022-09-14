"""
while True:
    pi = 3.141592
    print('=' * 50, 'CALCULE ÁREA DO CILINDRO CÍRCULAR:', '=' * 50)
    a = float(input('Informe a altura do cilindro em centímetros:'))
    r = float(input('Informe o raio do cilindro em centímetros:'))
    volume = pi * r**2 * a
    print(f'O volume do cilíndro circular é {volume:.2f} cm3!')
"""
pi = 3.141592
while True:
    print('%' * 50, 'Volume do cilindro', '%' * 50)
    raio = float(input('Insira o valor do raio em centímetros:'))
    altura = float(input('Insira o valor da altura em centímetros:'))
    v = ((raio ** 2) * pi) * altura
    print(f'O valor do volume do cilindro circular é {v:.2f} cm².')
