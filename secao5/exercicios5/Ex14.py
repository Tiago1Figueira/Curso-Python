"""
peso1 = 2
peso2 = 3
peso3 = 5
while True:
    print('=' * 75, 'CÁLCULO DA MÉDIA!', '=' * 75)
    laboratorio1 = float(input('Informe a nota laboratório de 0 a 10:'))
    semestral2 = float(input('Informe a nota semestral de 0 a 10:'))
    exame_final3 = float(input('Informe a nota exame final de 0 a 10:'))
    media_ponderada = (laboratorio1 * peso1 + semestral2 * peso2 + exame_final3 * peso3) / (peso1 + peso2 + peso3)
    print(f'A média ponderada é {media_ponderada}!!')
    if media_ponderada <= 2.9:
        print('Aluno reprovado!')
    elif media_ponderada >= 3 and media_ponderada <= 4.9:
        print('Aluno de recuperação!')
    else:
        print('Aluno aprovado!')
"""
peso_lab = 2
peso_aval = 3
peso_exame = 5
while True:
    print('%' * 150)
    nota_lab = float(input('Insira a nota de laboratório:'))
    while nota_lab < 0 or nota_lab > 10:
        print('Nota de laboratório inválida!')
        nota_lab = float(input('Insira a nota de laboratório:'))
    nota_aval = float(input('Insira a nota de avaliação:'))
    while nota_aval < 0 or nota_aval > 10:
        print('Nota de avaliação inválida!')
        nota_aval = float(input('Insira a nota de avaliação:'))
    nota_exame = float(input('Insira nota do exame: '))
    while nota_exame < 0 or nota_exame > 10:
        print('Nota de exame final inválida!')
        nota_exame = float(input('Insira nota do exame: '))
    media = (nota_lab * peso_lab + nota_aval * peso_aval + nota_exame * peso_exame) / (
                peso_lab + peso_aval + peso_exame)
    print(f'Média {media:.2f}')
    if media <= 2.9:
        print('aluno reprovado! ')
    elif media >= 3.0 and media <= 4.9:
        print('aluno de recuperação!')
    else:
        print('aluno aprovado!')
