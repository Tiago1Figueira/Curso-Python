# não fiz esse, mas somente o copiei!
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Exemplo de chamada da função:
resultado = fibonacci(6)
print(resultado)  # saída: 8
