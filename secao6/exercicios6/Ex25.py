"""
#1
soma = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        soma += i # coloque print(i) antes do código soma para saber quais são os números que serão somados.
        print(soma)

#2
soma = 0
for i in range(1, 1001):
    if i % 3 == 0 or i % 5 == 0:
        soma += i
print(soma)

#3
soma = 0
for i in range(1,1001):
    if i % 3 == 0 or i % 5 == 0 :
        soma += i
    print(soma)


soma = 0
n = 1000
print('%' * 50, 'CALCULA E MOSTRA TODOS OS DIVISORES DE 1000 POR 3 OU 5:', '%' * 50)
for i in range(0, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        soma += i
print(soma)
"""
soma = 0
print('%' * 50, 'CALCULA E MOSTRA TODOS OS DIVISORES'
                ' DE 1000 POR 3 OU 5:', '%' * 50)
for numero in range(1, 1001):
    if numero % 3 == 0 or numero % 5 == 0:
        soma += numero
print(f'{soma}')
