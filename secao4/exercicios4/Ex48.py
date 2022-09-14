"""
while True:
    print('=' * 150)
    valor = int(input('Informe um valor em segundos:'))
    hora = int(valor / 3600)
    rest_seg = valor % 3600
    minutos = int(rest_seg / 60)
    segundos = rest_seg % 60
    print(f'O número de {valor} segundos é igual a {hora}:{minutos}:{segundos}!')

#2
while True:
    print('=' * 150)
    segundos = int(input('Informe a quantidade em segundos:'))
    horas = int(segundos / 3600)
    rest_segundos = segundos % 3600
    minutos = int(rest_segundos / 60)
    segundos1 = rest_segundos % 60
    print(f'{segundos} segundos são iguais a {horas}:{minutos}:{segundos1}!')

"""
while True:
    print('%' * 150)
    segundos = int(input('Insira o valor em segundos:'))
    minutos = segundos / 60
    horas = segundos / 3600
    print(f'O valor dado é igual a {segundos} segundos ou {minutos:.2f} minutos ou {horas:.2f} horas.')




















