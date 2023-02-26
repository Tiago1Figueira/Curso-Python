"""
#1
lista = []
for i in range(1,11):
    num = float(input(f'Informe o {i}° número:'))
    lista.append(num)
print(f'O maior valor da lista é {max(lista)} e o menor valor é {min(lista)}! ')

#2
vetor = [ ]
while True:
    print('='*80)
    for i in range(1,11):
        num = float(input(f'Informe o {i}° número:'))
        while num != int(num):
            print('Número inválido!')
            num = float(input(f'Informe o {i}° número:'))
        vetor.append(num)
    print(f'Maior número {max(vetor)}\nMenor número {min(vetor)}!')
"""
vetor = []
while True:
    print('=' * 80, 'RECEBE E MOSTRA O MAIOR E MENOR VALOR DIGITADO!', '=' * 80)
    for i in range(1, 11):
        numero = input(f'Informe o {i}° número:')
        try:
            numero = float(numero)
            vetor.append(numero)
        except:
            print('Caracter inválido! Tente novamente!')

    print(f'Maior valor digitado:{max(vetor)}\n'
          f'Menor valor digitado:{min(vetor)}')

    vetor.clear()
