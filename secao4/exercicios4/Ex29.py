"""
while True:
        nota1 = float(input(f'Informe a 1ª nota:'))
        nota2 = float(input(f'Informe a 2ª nota:'))
        nota3 = float(input(f'Informe a 3ª nota:'))
        media_aritmetica = (nota1 + nota2 + nota3) / 3
        print(f'A média aritmética das notas é {media_aritmetica}!')

"""
while True:
    print('%' * 50, 'MÉDIA ARITMÉTICA', '%' * 50)
    soma = 0
    media = 0
    for i in range(1, 5):
        nota = float(input(f'Insira a {i}ª nota:'))
        soma += nota
        media = soma / 4
    print(f'A média aritmética das notas é igual a {media:.2f}.')

