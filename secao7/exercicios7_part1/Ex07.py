"""
#1
vetor = []
for i in range(1,11):
    num = float(input(f'Informe o {i}° número:'))
    vetor.append(num)
print(vetor)
print(max(vetor))
print(vetor.index(max(vetor)))

#2
vetor = [ ]
while True:
    print('='*80)
    for i in range(1,11):
        num = float(input(f'Informe o {i}° número:'))
        vetor.append(num)
    print(f'Números digitados: {vetor}\nMaior elemento: {max(vetor)}\nPosição Maior elemento: {vetor.index(max(vetor))}')
    vetor.clear()

"""
vetor = []
while True:
    print('=' * 50, 'IMPRIME O MAIOR NÚMERO RECEBIDOS DE 10 E O IMPRIME JUNTAMENTE COM O VALOR DA SUA POSIÇÃO!', '=' * 80)
    for i in range(1, 11):
        num = float(input(f'Insira o {i}° número: '))
        while num != int(num):
            print('Valor inválido! Digite somente números inteiros!')
            num = float(f'Insira o {i}° número: ')
        vetor.append(num)
    print(f'Números digitados: {vetor}\nMaior elemento: {max(vetor)}\n'
          f'Posição do maior número {vetor.index(max(vetor))}')

    vetor.clear()



