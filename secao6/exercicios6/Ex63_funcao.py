"""
# 1
def somarDoisNumeros(a, b):
    total = a + b
    return total


numero1 = int(input('Insira o primeiro número:'))
numero2 = int(input('Insira o segundo número:'))

print(somarDoisNumeros(numero1, numero2))


# 2
def funcaoSemRetorno(texto):
    print('Olá', texto, 'meu nome é Tiago!')


funcaoSemRetorno('João')

# 3
a = 3
b = 6


def multiplicacaoDoisNumeros(a, b):
    multiplicacao = a * b
    return multiplicacao


print(multiplicacaoDoisNumeros(a, b))

"""

# 4
def funcaoSemRetorno(texto):
    print('Olá', texto, 'meu nome é Tiago!')


nome = funcaoSemRetorno('Joao')

print(nome)
"""
e eu dei um print na variável nome, e ela tá com o valor None
ou seja, como a função não tem return, e o print não é um retorno válido , 
no lugar da variável 'nome' num foi guardado nada.
essa que é a diferença... usando return eu poderia guardar algo ali na variável nome 
e usar depois pra qualquer outra coisa

"""