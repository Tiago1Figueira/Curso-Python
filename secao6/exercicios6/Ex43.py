"""
#1
soma = 0
media = 0
cont = 0
lista = []
idade = int(input('Informe a sua idade:'))
while idade != 0:
    idade = int(input('Informe a sua idade:'))
    soma += idade
    cont += 1
    media = soma / cont
    lista.append(idade)
print(f'Média das idades desse grupo é {media:.2f} e as idades informadas são {lista}')
# a primeira idade informada não está sendo usada no cálculo. Por quê?

#2
media = 0
soma = 0
cont = 0
idade = int(input('Informe a sua idade:'))
soma += idade
cont += 1
while idade > 0:
    idade = int(input('Informe a sua idade:'))
    soma += idade
    cont += 1
    if idade == 0:
        print('Programa finalizado!')
        break
    media = soma / cont
print(f'A idade média desse grupo é {media:.2f}!')


#3
idades = [ ]
while True:
    num = float(input('Informe sua idade:'))
    while num != int(num):
        print('Idade inválida!')
        num = float(input('Informe sua idade:'))
    if num <= 0:
        print('Você saiu!')
        break
    else:
        idades.append(num)
print(f'A idade média desse grupo é {sum(idades)/ len(idades)}!')
"""
somaIdade = 0
cont = 0
mediaIdades = 0
print('#' * 50, 'SOMA IDADES E MOSTRA A MÉDIA DELAS', '#' * 50)
while True:
    idade = input('Insira a sua idade:')
    cont += 1
    try:
        idade = int(idade)
        if idade > 0:
            somaIdade += idade
            mediaIdades = somaIdade / cont
        else:
            print('Idade nula ou negativa!Você saiu!\n')
            break
    except:
        print('Caracter inválido! Tente novamente!')

print(f'Idades Somadas = {somaIdade}, '
    f'Média idades= {mediaIdades}')
