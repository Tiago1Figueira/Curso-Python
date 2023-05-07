"""
#1
notas = []
cont = 0
valores = 0
media = ' '
for i in range(1,5):#16
    num = float(input(f'Informe o {i}° nota:'))
    notas.append(num)
    notas.sort( )
    cont += 1
    valores += num
    #media = valores / cont
    media = sum(notas) / len(notas)

print(f'As notas são {notas} e a média geral das notas é {media:.2f}!')


#2
notas = [ ]
for i in range(1,16):
    num = float(input(f'Informe o {i}° número:'))
    while num < 0 or num > 10:
        print('Nota inválida!')
        num = float(input(f'Informe o {i}° número:'))
    notas.append(num)
print(f'Média {sum(notas) / len(notas)}!')

"""

nota = []
while True:
    print('=' * 50, 'IMPRIME A MÉDIA GERAL DE UMA SALA DE 15 ALUNOS!', '=' * 80)
    for i in range(1, 16):
        num = float(input(f'Informe a {i}° nota:'))
        while num < 0 or num > 10:
            print('Nota inválida!')
            num = float(input(f'Informe a {i}° nota:'))
            nota.append(num)
    print(f'Media {sum(nota) / len(nota)}!!')
