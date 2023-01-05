"""
#1
soma = 0
fatorial = 1
n = int(input('Informe um número:'))
while n <=0:
    n = int(input('Informe um número:'))
for i in range(1, n+1):
    fatorial = fatorial * i
    soma += fatorial
    E = 1 + 1 / fatorial # aqui n é fatorial!
print(f'O número {n} gera o número E={E}.')
# conferir com o professor se o código está correto.

#2
"""
fatorial = 1
e = 1
print('%' * 50, 'CALCULA O VALOR DA FUNÇÃO "E" ', '%' * 50)
# Entrada
n = float(input('Informe um número positivo e inteiro:'))

if n <= 0 or n != int(n):
    print('Valor inválido! Tente novamente!')

else:
    n = int(n)
    for i in range(1, n + 1):
        fatorial = fatorial * i
        e = e + (1 / fatorial)
    print(f'Fatorial = {fatorial}\nE = {e:.2f}')
