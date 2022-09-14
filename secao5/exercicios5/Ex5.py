"""
while True:
    num = int(input('Informe um número:'))
    if num % 2 == 0:
        print(f'O número {num} é par!! ')
    else:
        print(f'O número {num} é ímpar!!')
"""

while True:
    print('%' * 150)
    num = int(input('Insira um número inteiro e positivo:')) # inseri-se o float e não int p/que haja resposta qdo de números decimais!!
    while num < 0: # usa-se o while e não if para que haja a repetição da pergunta.
        print('Favor inserir número positivo e inteiro!')
        num = int(input('Insira um número:'))
    if num % 2 == 0:
        print(f'{num} é par!')
    else:
        print(f'{num} é ímpar!!')
