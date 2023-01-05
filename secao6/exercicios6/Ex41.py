"""
#1
lista = []
r1 = ' '
r2 = ' '
while True:
    r1 = float(input('Informe a resistência 1:'))
    if r1 <= 0:
        print('Você finalizou')
        break
    r2 = float(input('Informe a resistência 2:'))
    if r2 <= 0:
        print('Você finalizou')
        break
    r = r1 * r2 / r1 + r2
    lista.append(r)
    print(lista)
    lista.clear()

#2
while True:
    r1 = float(input('Informe a resistência 1:'))
    if r1 <=0:
        print('Número inválido! Você saiu!')
        break
    r2 = float(input('Informe a resistência 2:'))
    if r2 <= 0:
        print('Número inválido! Você saiu!')
        break
    r = r1 * r2 / r1 + r2
    print(r)
"""
resistencia = 0
while True:
    print('#' * 50, 'CALCULA A RESISTÊNCIA USANDO OS RESISTORES R1 e R2', '#' * 50)
    r1 = float(input('Insira a resistência 1:'))
    r2 = float(input('Insira a resistência 2:'))
    if r1 == 0 or r2 == 0:
        break
    else:
        resistencia = resistencia + ((r1 * r2) / (r1 + r2))
print(f'Resistência = {resistencia:.3f}')
