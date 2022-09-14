"""
#Aqui a análise do ano bissexto é usada para apoiar uma condição.
#(análise de condições e dentre elas de ser ano bissexto!)

bisexto = False
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    bisexto = True

while True:
    print('=' * 50, 'ANO É BISSEXTO ?', '=' * 50)
    ano = int(input('Informe o ano:'))

    if ano % 400 == 0:
        print(f'O ano {ano} é bissexto!')
    elif ano % 4 == 0 and ano % 100 != 0:
        print(f'O ano {ano} é bissexto!')
    else:
        print(f'O ano {ano} não é bissexto!')
"""
while True:
    print('%' * 150)
    ano = float(input('Insira um ano:'))
    if ano % 400 == 0:
        print(f'{ano:.0f} é bissexto!')
    elif ano % 4 == 0 and ano % 100 != 0:
        print(f'{ano:.0f} é bissexto!')
    else:
        print(f'{ano:.0f} não é bissexto!')

