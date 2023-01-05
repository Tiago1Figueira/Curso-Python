"""
#1
n = 1
while True:
    check = 0
    for i in range(1, 21):                         # loop para construir o valor a ser checado
        check += n % i

    if check == 0:
        print(f'O menor divisível é: {n}.')
        break
    n += 1
"""
