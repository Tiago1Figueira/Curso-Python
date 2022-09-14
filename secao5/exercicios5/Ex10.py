"""
peso_ideal = ' '
while True:
    print('=' * 50,'CALCULE O SEU PESO IDEAL!','=' * 50)
    sexo = input('Informe h para homem ou m para mulher:   ')
    altura = float(input('Informe a sua altura:'))
    if sexo.lower() == 'h':
        peso_ideal = (72.7 * altura) - 58
        print(f'O seu peso ideal é {peso_ideal:.2f}!')
    elif sexo.lower() == 'm':
        peso_ideal = (62.1 * altura) - 44.7
        print(f'O seu peso ideal é {peso_ideal:.2f}!')
    else:
        print('=' * 50, 'Atenção: Favor informar h ou m!', '=' * 50)
        sexo = input('Informe h para homem ou m para mulher:')
        altura = float(input('Informe a sua altura:'))
        if sexo.lower() == 'h':
            peso_ideal = (72.7 * altura) - 58
            print(f'O seu peso ideal é {peso_ideal:.2f}!')
        elif sexo.lower() == 'm':
            peso_ideal = (62.1 * altura) - 44.7
            print(f'O seu peso ideal é {peso_ideal:.2f}!')
"""

while True:
    print('%' * 150)
    sexo = input('Informe o seu sexo: H(homem)ou M(mulher):')
    altura = float(input('Informe a sua altura:'))
    if sexo.lower() == 'h':
        homem = (72.7 * altura) - 58
        print(f'O seu peso ideal é {homem:.2f}.')
    elif sexo.lower() == 'm':
        mulher = (62.1 * altura) - 44.7
        print(f'O seu peso ideal é {mulher:.2f}.')



