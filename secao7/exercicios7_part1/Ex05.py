"""
#1
lista = []
pares = []
for i in range(1,11):
    num = int(input(f'Informe o {i}° número:'))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
        len(pares)
print(pares)
print(f'Neste grupo de números há {len(pares)} valores pares.')


#2
pares = [ ]
while True:
    print('='*80)
    for i in range(1,5):
        num = float(input(f'Informe o {i}° número:'))
        while num != int(num):
            print('Número inválido!')
            num = float(input(f'Informe o {i}° número:'))
        if int(num) % 2 == 0:
            pares.append(num)
    print(f'Quantia de números pares: {len(pares)}\nNúmeros pares: {pares}')
    pares.clear()

"""
pares = []
while True:
    print('#' * 50, 'RECEBE 10 VALORES E MOSTRA SOMENTE OS PARES', '#' * 50)
    for i in range(1, 11):
        numero = input(f'Informe o {i}° número:')
        try:
            numero = float(numero)
            if numero % 2 == 0:
                pares.append(numero)

        except:
            print('Caracter inválido!Tente novamente!')
    print(f'Números pares digitados:{pares}')
    pares.clear()
