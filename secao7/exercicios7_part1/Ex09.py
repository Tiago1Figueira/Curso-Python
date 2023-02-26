"""
#1
lista = []
pares = []
for i in range(1,7):
    num = int(input(f'Informe o {i}° número par:'))
    while num % 2 != 0:
        num = int(input(f'Informe o {i}° número par:'))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
# 2 formas de fazer a reversão:
print(lista)
print(pares[::-1])

pares.reverse()
print(pares)

#2
pares = [ ]
for i in range(1,7):
    num = float(input(f'Informe o {i}° número:'))
    while num != int(num):
        print('Número inválido!')
        num = float(input(f'Informe o {i}° número:'))
    pares.append(num)
pares.sort()
print(pares[::-1])
"""
vetor = []
while True:
    print('=' * 50, 'IMPRIME OS 6 NÚMEROS PARES RECEBIDOS NA ORDEM INVERSA!', '=' * 80)
    for i in range(1, 7):
        num = input(f'Insira o {i}º primeiro número inteiro:')
        try:
            num = int(num)
            if num % 2 == 0:
                vetor.append(num)
            else:
                print('Deve ser número par!Tente novamente!')
        except:
            print('Caracter inválido! Tente novamente!')
    print(f'{vetor[::-1]}')
    vetor.clear()
