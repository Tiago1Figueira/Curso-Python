"""
# tá dando data inválida 2 para todas as datas!
bissexto = False
while True:
    print('=' * 150)
    dia = int(input('Informe um dia:'))
    mes = int(input('Informe um mes:'))
    ano = int(input('Informe um ano:'))
    if dia < 1 or dia > 31:
        print(f'{dia}/{mes}/{ano}')
        print('Data inválida! 1')
    elif dia == 31 and mes != 1 or mes != 3 or mes != 5 or mes != 7 or mes != 8 or mes != 10 or mes != 12:
        print(f'{dia}/{mes}/{ano}')
        print('Data inválida! 2')
    elif dia == 30 and mes != 2 or mes != 4 or mes != 6 or mes != 9 or mes != 11:
        print(f'{dia}/{mes}/{ano}')
        print('Data inválida! 3')
    elif ano % 400 == 0 or ano % 100 != 0 and ano % 4 == 0: # identifica o ano bissexto!!
        bissexto = True
    elif dia == 29 and mes == 2 and bissexto == False :
        print(f'{dia}/{mes}/{ano}')
        print('Data inválida! 4')
    elif dia < 29 and mes == 2:
        print(f'{dia}/{mes}/{ano}')
        print('Data inválida! 5')
    elif mes < 1 or mes > 12:
        print(f'{dia}/{mes}/{ano}')
        print('Data Inválida! 6')
    elif ano < 1000 or ano > 9999:
        print(f'{dia}/{mes}/{ano}')
        print('Data inválida! 7')
    else:
        print(f'{dia}/{mes}/{ano}')
        print('Data válida!')
"""
while True:
    print('%' * 50, 'CÁLCULO DE DATA VÁLIDA', '%' * 50)
    dia = int(input('Informe o dia do aniversário:'))
    while dia <= 0 or dia > 31:
        print('Dia inválido!')
        dia = int(input('Informe o dia do aniversário:'))
    mes = int(input('Informe o mês do aniversário:'))
    while mes <= 0 or mes > 12:
        print('Mês inválido!')
        mes = int(input('Informe o mês do aniversário:'))
    ano = int(input('Informe o ano do aniversário:'))
    while ano <= 0 or ano > 9999:
        print('Ano inválido!')
        ano = int(input('Informe o ano do aniversário:'))

    bissexto = False
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        bissexto = True
    while dia >= 30 and mes == 2:
        print('Dia inválido!')
        dia = int(input('Informe o dia do aniversário:'))
    while dia == 29 and mes == 2 and bissexto == False:
        print('Dia inválido!')
        dia = int(input('Informe o dia do aniversário:'))
    while dia == 30 and mes != 4 and mes != 6 and mes != 9 and mes != 11:
        print('Mês inválido!')
        mes = int(input('Informe o mês do aniversário:'))
    while dia == 31 and mes != 1 and mes != 3 and mes != 5 and mes != 7 and mes != 8 and mes != 10 and mes != 12:
        print('Mês inválido!')
        mes = int(input('Informe o mês do aniversário:'))
    else:
        print(f'{dia}/{mes}/{ano} - Data válida!')
