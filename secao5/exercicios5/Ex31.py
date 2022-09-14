"""
while True:
    altura = float(input('Informe a altura:'))
    peso = float(input('Informe o peso:'))

    if peso < 60 and altura < 1.20:
        print("A")
    elif peso < 60 and altura >= 1.20 and altura <= 1.70:
        print("B")
    elif peso < 60 and altura > 1.70:
        print("C")

    elif peso >= 60 and peso <= 90 and altura < 1.20:
        print("D")
    elif peso >= 60 and peso <= 90 and altura >= 1.20 and altura <= 1.70:
        print("E")
    elif peso >= 60 and peso <= 90 and altura > 1.70:
        print("F")

    elif peso > 90 and altura < 1.20:
        print("G")
    elif peso > 90 and altura >= 1.20 and altura <= 1.70:
        print("H")
    elif peso > 90 and altura > 1.70:
        print("I")
"""
while True:
    print('%' * 150)
    peso = float(input('Insira o peso em kg:'))
    altura = float(input('Insira a altura em centímetros:'))
    if peso <= 60 and altura < 120:
        print('Classificação A!')
    elif peso <= 60 and altura >= 120 and altura <= 170:
        print('Classificação B!')
    elif peso <= 60 and altura > 170:
        print('Classificação C!')
    elif peso > 60 and peso <= 90 and altura < 120:
        print('Classificação D!')
    elif peso > 60 and peso <= 90 and altura >= 120 and altura <= 170:
        print('Classificação E!')
    elif peso > 60 and peso <= 90 and altura > 170:
        print('Classificação F!')
    elif peso > 90 and altura < 120:
        print('Classificação G!')
    elif peso > 90 and altura >= 120 and altura <= 170:
        print('Classificação H!')
    elif peso > 90 and altura > 170:
        print('Classificação I!')
    else:
        print('Valores inválidos! Vocês saiu!')
        break
