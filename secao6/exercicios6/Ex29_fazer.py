"""
#aqui usa-se import!

import math
s = 0
num = int(input('Digite um número inteiro\nn = '))
for n in range(1, num + 1):
    s = s + n / (math.factorial(n * 2))

print('O resultado desta série é ', s)

"""

while True:
    n = float(input('Insira um número:'))
    if n <= 0 or n != int(n):
        print('Valor inválido!Tente novamente!')
   # else:




