"""
#1
soma = 0
cont = 0
print('Para sair do programa digite notas menores que 10 e maiores que 20!')
nota = float(input('Informe a nota da prova:'))
while nota >= 10 and nota <= 20:
    nota = float(input('Informe a nota da prova:'))
    soma += nota
    cont += 1
    media = soma / cont
print(f'A média é {media:.2f}!')
# como fazer para que a nota que finalizará o programa não ser contada para efeito do cálculo da média?

#2
soma = 0
cont = 0
print('Para sair do programa digite notas menores que 10 e maiores que 20!')
nota = float(input('Informe a nota da prova:'))
while nota >= 10 and nota <= 20:
    nota = float(input('Informe a nota da prova:'))
    if nota < 10 or nota > 20:
        break
    soma += nota
    cont += 1
    media = soma / cont
print(f'A média é {media:.2f}!')
# com o if + break sugerido pelo professor!

#3
soma = 0
cont = 0
print('Para sair do programa digite notas menores que 10 e maiores que 20!')
nota = float(input('Informe a nota da prova:'))
while True:
    nota = float(input('Informe a nota da prova:'))
    if nota >= 10 and nota <= 20:
        soma += nota
        cont += 1
        media = soma / cont
    else:
        break
print(f'A média é {media:.2f}!')

#4
soma = 0
cont = 0
print('Digite nota menor que 10 ou maior que 20 para finalizar programa e obter a média das notas!')
nota =float(input('Informe a nota:'))
while True:
    nota = float(input('Informe a nota:'))
    if nota >= 10 and nota <= 20:
        cont += 1
        soma += nota
        media = soma / cont
    else:
        break
print(f'A média das notas digitadas será {media}')

#5
notas = []
media = ' '
while True:
    print('='*80)
    print('Notas fora de 10 e 20 finalizam programa!')
    nota = float(input('Informe um nota entre 10 e 20:'))
    if nota >= 10 and nota <= 20:
        notas.append(nota)
        media = sum(notas) / len(notas)
    else:
        break
print(f'A média das notas é {media:.2f}!')


soma = 0
cont_1 = 0
cont_2 = 0
cont_total = 0
media = 0
while True:
    print('%' * 50, 'CALCULA A MÉDIA ARITMÉTICA DAS NOTAS DOS ALUNOS:', '%' * 50)
    notas = float(input('Insira notas entre 10 e 20:'))
    cont_1 = cont_1 + 1
    while notas >= 10 and notas <= 20:
        notas = float(input('Insira notas entre 10 e 20:'))
        cont_2 = cont_2 + 1
        soma = soma + notas
        cont_total = cont_1 + cont_2
        media = soma / cont_total
    else:
        print('Nota inválida!')
        print('Você saiu!')
        break
print(f'A média aritmética das {cont_total} notas é {media:.2f}.')
"""
#VAR
soma = 0
cont = 0
media = 0
print('%' * 50, 'CALCULA A MÉDIA ARITMÉTICA DAS NOTAS DOS ALUNOS:', '%' * 50)
while True:
#ENTRADA
    nota = float(input('Insira a sua nota entre 10 e 20:'))
#PROCESSAMENTO
    if nota >= 10 and nota <= 20:
        soma += nota
        cont += 1
        media = soma/cont
    else:
        print('Nota inválida!')
        print('Você saiu!')
        break
#SAÍDA
print(f'Soma: {soma}\nContador:{cont}\nMédia:{media}')
