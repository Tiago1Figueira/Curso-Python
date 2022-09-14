"""
peso1 = 1
peso2 = 2
print('=' * 50, 'CÁLCULO MÉDIA PONDERADA!', '=' * 50)
while True:
    nota1 = float(input(f'Informe a 1ª nota de 0 a 100:'))
    nota2 = float(input(f'Informe a 2ª nota de 0 a 100:'))
    nota3 = float(input(f'Informe a 3ª nota de 0 a 100:'))
    media_ponderada = (nota1 * peso1 + nota2 * peso1 + nota3 * peso2) / (peso1 + peso1 + peso2)

    print(f'A média ponderada das notas é igual a {media_ponderada}!!')
    if media_ponderada >= 60:
        print('Aluno aprovado!')
        print('=' * 50, 'CÁLCULO MÉDIA PONDERADA!', '=' * 50)
    else:
        print('Aluno reprovado!')
        print('=' * 50, 'CÁLCULO MÉDIA PONDERADA!', '=' * 50)
"""
peso1 = 1
peso2 = 1
peso3 = 2
while True:
    nota1 = float(input('Insira o valor da 1ª nota:'))
    while nota1 < 0 or nota1 > 100:
        print('Nota 1 inválida! Favor inserir nota entre 0 a 100!')
        nota1 = float(input('Insira o valor da 1ª nota:'))
    nota2 = float(input('Insira o valor da 2ª nota:'))
    while nota2 < 0 or nota2 > 100:
        print('Nova 2 inválida! Favor inserir nota entre 0 a 100!')
        nota2 = float(input('Insira o valor da 2ª nota:'))
    nota3 = float(input('Insira o valor da 3ª nota:'))
    while nota3 < 0 or nota3 > 100:
        print('Nova 3 inválida! Favor inserir nota entre 0 a 100!')
        nota3 = float(input('Insira o valor da 3ª nota:'))
    media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
    if media_ponderada > 60:
        print(f'Média ponderada = {media_ponderada} - Aluno aprovado!')
    else:
        print(f'Média ponderada = {media_ponderada} - Aluno reprovado!')
