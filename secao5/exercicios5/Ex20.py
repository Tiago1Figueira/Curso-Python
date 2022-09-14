"""
#1
def calculo_triangulo(a,b,c):

    if a == 0 or b == 0 or c == 0:
        return 'Todos os lados devem ser maiores que 0!'
    if a >= b + c:
        return f'A figura plana não é um triângulo!'
    if b >= a + c:
        return f'A figura plana não é um triângulo!'
    if c >= a + b:
        return f'A figura plana não é um triângulo!'
    if a != b and a != c and b != c:
        return f'Triângulo Escaleno!'
    if a == b and a == c and b == c:
        return f'Triângulo Equilátero!'
    return f'Triângulo Isósceles!'
while True:
    a = float(input('Informe o valor lado 1:'))
    b = float(input('Informe o valor lado 2:'))
    c = float(input('Informe o valor lado 3:'))
    print(calculo_triangulo(a,b,c))

#2
while True:
    print('=' * 50, 'DESCUBRA O TIPO DE TRIÂNGULO:', '=' * 50)
    a = int(input('Informe lado A do triângulo:'))
    b = int(input('Informe lado B do triângulo:'))
    c = int(input('Informe lado C do triângulo:'))
    if a == 0 or b == 0 or c == 0:
        print('Todos os lados devem ser maiores que 0!')
    elif a >= b + c:
        print('A figura plana não é um triângulo!')
    elif b >= a + c:
        print('A figura plana não é um triângulo!')
    elif c >= b + a:
        print('A figura plana não é um triângulo!')
    elif a != b and a != c and c != b:
        print('Triângulo Escaleno!')
    elif a == b and a == c and c == b:
        print('Triângulo Equilátero!')
    else:
        print('Triângulo Isósceles!')

"""
while True:
    print('%' * 150)
    a = float(input('Insira o valor do lado A do triângulo:'))
    b = float(input('Insira o valor do lado B do triângulo:'))
    c = float(input('Insira o valor do lado C do triângulo:'))
    if a == 0 or b == 0 or c == 0:
        print('Para ser um triângulo os valores de A, B ou C devem ser diferentes de 0!')
        break
    elif a >= b + c:
        print('O valor de A não pode ser usado como lado de um triângulo!')
        break
    elif b >= a + c:
        print('O valor de B não pode ser usado como lado de um triângulo!')
        break
    elif c >= a + b:
        print('O valor de C não pode ser usado como lado de um triângulo!')
        break
    elif a == b and b == c and c == a:
        print(f'O triângulo ABC é equilátero.')
    elif a == b or b == c or c == a:
        print(f'O triângulo ABC é isósceles.')
    else:
        print(f'O triângulo ABC é escaleno.')
