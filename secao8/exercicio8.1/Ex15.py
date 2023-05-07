def juros_compostos(capital, taxa, tempo):
    montante = capital * (1 + (taxa / 100)) ** tempo
    return montante


# Exemplo de chamada da função:
resultado = juros_compostos(1000, 10, 6)
print(resultado)
