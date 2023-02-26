"""
#1
vetor1 = []
vetor_quadrado = []
for i in range(1, 11):
    num = float(input(f'Informe o {i}° número real:'))
    vetor1.append(num)
print(vetor1)
for i in vetor1:
    quadrado = i **2
    vetor_quadrado.append(quadrado)
print(vetor_quadrado)

#2
vetor = [ ]
vetor_quadrado = [ ]
while True:
    print('='*80)
    for i in range(1,5):
        num = float(input(f'Informe o {i}° número:'))
        vetor.append(num)
    for i in vetor:
        quadrado = i ** 2
        vetor_quadrado.append(quadrado)
    print(f'Números digitados {vetor}!\nNúmeros ao quadrado {vetor_quadrado}!')
    vetor.clear()
    vetor_quadrado.clear()
"""
vetor = []
vetorQuadrado = []
while True:
    for elementos in range(1, 11):
        numero = float(input(f'Informe o {elementos}° número:'))
        vetor.append(numero)
    for elementos in vetor:
        quadrado = elementos ** 2
        vetorQuadrado.append(quadrado)
    print(f'Elementos digitados:{vetor}\n'
          f'Quadrado dos Elementos:{vetorQuadrado}')
    vetor.clear()
    vetorQuadrado.clear()