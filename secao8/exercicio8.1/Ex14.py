def juros_simples(capital, taxa, tempo):
    juros = capital * (taxa / 100) * tempo
    return juros + capital


resultado = juros_simples(1000, 7, 3)
print(resultado)
