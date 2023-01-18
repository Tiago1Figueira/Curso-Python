"""
# checar se está certo!!
#1
salario = 2000
taxa = 0.015
ano = 1995
ano_atual = 2019

while ano < ano_atual:
    ano += 1
    salario = (salario * taxa) + salario
    print(f'Ano = {ano}, Salário = R$ {salario:.2f}, Taxa = {100 * taxa}%')  # Para 'DEBUG'
    taxa = taxa * 2

print(f'Em {ano} o salário será de R$ {salario:.2f}.')

#2
t = 0.75
salario = 2000
ano1 = 1995
ano2 = 2021
while ano1 < ano2:
    salario += (2 * t)
    t += t * 2
    ano1 += 1
print(f'O valor do salário em {ano2} será de {salario:.2f} reais!')


#3
sal = 2000
aumento = 0.75
ano = 1995
while ano < 2021:
    sal += sal + (aumento * 2 )
    aumento = aumento * 2
print(f'{sal:.2f}')
print(ano)


a = 1997
taxa1997 = 0.030
sal1995 = 2000
sal1996 = sal1995 + (sal1995 * 0.015)
sal1997 = sal1996 + (sal1996 * 0.030)

while a <= 2022:
    taxa1997 *= 2
    sal2022 = sal1997 + (sal1997 * taxa1997)


    print(f'O valor do salário atual é {sal2022}')
"""

