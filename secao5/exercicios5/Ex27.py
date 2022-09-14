"""
while True:
    print('='* 50, "CATEGORIA DO NADADOR", '=' * 50)
    idade = int(input('Informe a idade do nadador:'))
    if idade < 5:
        print('Muito Jovem!')
    if idade >=5 and idade <=7:
        print(f'Categoria Infantil A!')
    if idade >=8 and idade <=10:
        print('Categoria Infantil B!')
    if idade >=11 and idade <= 13:
        print('Categoria Juvenil A!')
    if idade>=14 and idade <=17:
        print('Categoria Juvenil B!')
    if idade>=18:
        print('Categoria Sênior!')
"""
while True:
    print('%' * 150)
    idade = float(input('Insira a sua idade:'))
    while idade < 5:
        print('Idade inválida! Informar idade igual ou acima de 5 anos!')
        idade = float(input('Insira a sua idade:'))
    if idade >= 5 and idade <= 7:
        print('INFANTIL A')
    elif idade >= 8 and idade <= 10:
        print('INFANTIL B')
    elif idade >= 11 and idade <= 13:
        print('JUVENIL A')
    elif idade >= 14 and idade <= 17:
        print('JUVENIL B')
    else:
        print('SÊNIOR')

