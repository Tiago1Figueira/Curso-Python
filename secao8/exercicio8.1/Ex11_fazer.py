# Não fiz esse, mas somente o copiei!!
def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Exemplo de chamada da função:
resultado = primo(7)
print(resultado)  # saída: True
