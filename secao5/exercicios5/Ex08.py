"""
while True:
    nota1 = float(input('Informe a 1ª nota:'))
    nota2 = float(input('Informe a 2ª nota:'))
    soma = nota1 + nota2
    media = soma / 2
    print(f'A média das notas é {media}!')
    print('=' * 150)
    if nota1 < 0 or nota1 > 10:
        print('Atenção: 1ª nota é inválida!')
        print('Você saiu do programa!!')
        break
    if nota2 < 0 or nota2 > 10:
        print('Atenção a 2ª nota é inválida!')
        print('Vocẽ saiu do programa!!')
        break
"""

while True:
    nota1 = float(input('Informe a 1ª nota:'))
    nota2 = float(input('Informe a 2ª nota:'))
    if nota1 < 0 or nota1 > 10:
        print('1ª nota inválida! Você saiu!')
        break
    elif nota2 < 0 or nota2 > 10:
        print('2ª nota inválida! Você saiu!')
        break
    else:
        media = (nota1 + nota2) / 2
        print(f'O valor da média é {media:.2f}.')
