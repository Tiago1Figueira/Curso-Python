"""
# como colocar aqui a restrição qdo o número for divisível por 3 e por 5.
num = int(input('Informe um número:'))
if num % 3 == 0 or num % 5 == 0 :
    print(f'O número {num} é divisível por 3 ou por 5!!')
else:
    print(f'O número {num} não é divisível por 3 ou por 5!!')
"""
while True:
    num = float(input('Informe o número:'))
    if num % 3 == 0:
        print(f'O número {num} é divisível por 3.')
    elif num % 5 == 0:
        print(f'O número {num} é divisível por 5.')
    else:
        print(f'O número {num} não é divisível por 3 nem por 5.')
