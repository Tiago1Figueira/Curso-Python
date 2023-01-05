"""
#1
divisao = 0
soma = 0
num = int(input('Informe um número:'))
while num <=0:
    num = int(input('Informe um número:'))
for i in range(1, num + 1):
    divisao += 1 / i
    soma += divisao
    h = 1 + 1 / soma
print(h)
# checar com o professor e ver se está correto.

#2
divisao = 0
h = 1
n = int(input('Informe um número inteiro e positivo:'))
while n < 0:
    n = int(input('Informe um número inteiro e positivo:'))
for i in range(1, n +1):
    divisao += 1 / i
    h = h + 1/divisao
print(f'O número harmônico de {n} é {h:.2f}!')

#3
h = ' '
soma = 0
while True:
    print('='*80)
    num = float(input('Informe um número inteiro e positivo:'))
    while num <= 0 or num != int(num):
        print('Número inválido!')
        num = float(input('Informe um número inteiro e positivo:'))
    for i in range(1, int(num) + 1):
        soma += 1 / i
        h = 1 + soma
    print(f'O número harmônico do número {num} é {h:.2f}!')

soma = 0
while True:
    print('%' * 50, 'CALCULA O VALOR DA FUNÇÃO HARMÔNICA', '%' * 50)
    n = float(input('Insira um número positivo e inteiro:'))
    while n <= 0 or n != int(n):
        print('Número inválido!')
        n = float(input('Insira um número positivo e inteiro:'))
    for i in range(1, int(n) + 1):
        soma += 1 / i
        h = 1 + soma
    print(f'O valor da função harmônica para o número {n} é {h:.2f}.')

h = 1
harmonica = 0
while True:
    print('%' * 50, 'CALCULA O VALOR DA FUNÇÃO HARMÔNICA', '%' * 50)
    #Entrada
    n = float(input('Informe um número positivo e inteiro:'))

    if n <= 0 or n != int(n) :
        print('Valor inválido! Tente novamente!')
    #Processamento
    else:
        n = int(n)
        if n == 1:
            harmonica = 1
        else:
            harmonica = 1
            for i in range(2, n + 1):
                harmonica = harmonica + (1/i)
    #Saída
        print(f'Número Harmônico:{harmonica:.2f}')
"""
print('Calcula a função harmônica de um número:')
numero = input('Insira um número positivo e inteiro :')
if (numero.isnumeric()):
    numero = int(numero)
    if (numero >= 1):
        harmonica = 1
        for i in range(2, numero + 1):
            harmonica = harmonica + (1 / i)
        print(f'Harmônica = {harmonica:.2f}')
    else:
        print('O valor digitado é negativo ou nulo!Tente novamente!')
else:
    print('O valor digitado não é um número ou contém caracteres inválidos! Tente novamente!')

