"""
while True:
    print('=' * 50, 'CALCULO DA NOTA:', '=' * 50)
    faltas = int(input('Informe quantas faltas o aluno tem:'))
    nota = float(input('Informe a nota do aluno:'))
    if faltas < 20:
        if 9 <= nota <= 10:
            print(f'O conceito desse aluno é A!')
        elif 7.5 <= nota <= 8.9:
            print(f'O conceito desse aluno é B!')
        elif 5 <= nota <= 7.4:
            print(f'O conceito desse aluno é C!')
        elif 4 <= nota <= 4.9:
            print(f'O conceito desse aluno é D!')
        elif 0 <= nota <= 3.9:
            print(f'O conceito desse aluno é E!')
        else:
            print('Nota inválida!')

    if faltas > 20:
        if 9 <= nota <= 10:
            print(f'O conceito desse aluno é B!')
        elif 7.5 <= nota <= 8.9:
            print(f'O conceito desse aluno é C!')
        elif 5 <= nota <= 7.4:
            print(f'O conceito desse aluno é D!')
        elif 4 <= nota <= 4.9:
            print(f'O conceito desse aluno é E!')
        elif 0 <= nota <= 3.9:
            print(f'O conceito desse aluno é E!')
        else:
            print('Nota inválida!')
"""
while True:
    print('%' * 150)
    nota = float(input('Insira a sua nota:'))
    while nota < 0 or nota > 10:
        print('Nota Inválida!')
        nota = float(input('Insira a sua nota:'))
    faltas = int(input('Insira o número de faltas:'))
    if faltas <= 20:
        if nota >=9 and nota <=10:
            print('Conceito A!')
        elif nota >=7.5 and nota <=8.9:
            print('Conceito B!')
        elif nota >=5 and nota <=7.4:
            print('Conceito C!')
        elif nota >= 4 and nota <=4.9:
            print('Conceito D!')
        else:
            print('Conceito E!')
    else:
        if nota >= 9 and nota <= 10:
            print('Conceito B!')
        elif nota >= 7.5 and nota <= 8.9:
            print('Conceito C!')
        elif nota >= 5 and nota <= 7.4:
            print('Conceito D!')
        elif nota >= 4 and nota <= 4.9:
            print('Conceito E!')
        else:
            print('Conceito E!')
