"""
#1
lista = []
num = int(input('Informe um número inteiro:'))
lista.append(num)
while num !=0 or num < 0:
    num = int(input('Informe um número inteiro:'))
    quadrado = num * num
    cubo = num ** 3
    raiz_quadrada = num ** 1/2
    lista.append(num)
    print(f'Número {lista}: seu é quadrado {quadrado}, seu cubo é {cubo} e sua raiz é {raiz_quadrada}')
# Por que o primeiro número inteiro não está aparecendo no print?

#2
lista = []
num = int(input('Informe um número maior que 0:'))
lista.append(num)
while True:
    if num > 0:
        num = int(input('Informe um número maior que 0:'))
        lista.append(num)
    else:
        print('Número negativo ou 0! Você finalizou o programa!')
        break
    quadrado = num * num
    cubo = num ** 3
    raiz_quadrada = num ** 1/2
    print('=' * 50, f'RESULTADOS PEDIDOS PARA NÚMERO {num}', '=' * 90)
    print(f'Números{lista}:quadrado:{quadrado}, cubo:{cubo}, raiz_quadrada:{raiz_quadrada}')
    print('=' *165)


#3
while True:
    print('='*80)
    num = float(input('Informe um número:'))
    if num <=0:
        print('Você saiu!')
        break
    else:
        quadrado = num * num
        cubo = num ** 3
        raiz_quadrada = num ** 0.5
    print(f'Quadrado {quadrado:.2f}, Cubo {cubo:.2f}, Raiz Quadrada {raiz_quadrada:.2f}!')

"""
while True:
    print('#' * 50, 'MOSTRA O QUADRADO, O CUBO E A RAIZ QUADRADA DE UM NÚMERO', '#' * 50)
    numero = input('Insira um número maior que 0:')
    try:
        numero = int(numero)
        if numero > 0:
            quadrado = numero * numero
            cubo = numero ** 3
            raizQuadrada = numero ** 0.5
            print(f'Quadrado= {quadrado}, '
                  f'Cubo= {cubo}, Raiz Quadrada= {raizQuadrada:.2f}')
        else:
            print('Número negativo ou nulo!Você saiu!')
            break
    except:
        print('Caracter inválido!')
