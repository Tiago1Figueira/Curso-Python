"""
lista = [ ]
while True:
    print("=" * 50,'CALCULE A SOMA DOS QUADRADOS DE 3 NÚMEROS', "=" * 50)
    for i in range(1,4):
        num = float(input(f'Informe o {i}° número:'))
        lista.append( (num)**2)

    print(f'O valor da soma dos números é {sum(lista)}!')
    lista.clear()
"""
while True:
    print("%" * 50, 'CALCULE A SOMA DOS QUADRADOS DE 3 NÚMEROS', "%" * 50)
    soma = 0
    for i in range(1, 4):
        n = float(input(f'Insira {i}º número:'))
        soma += (n) ** 2
    print(f'A soma dos quadrados dos 3 números é igual a {soma}.')
