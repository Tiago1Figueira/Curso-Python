"""
# print correto, contudo eu não me lembro pq eu coloquei 3 no range e assim deu certo!
n = int(input('Informe quantos múltiplos deseja ver na sequência:'))
i = int(input('Informe um número, inteiro e positivo,usado como múltiplo da sequência:'))
j = int(input('Informe outro número, inteiro e positivo,usado como múltiplo da sequência:'))
for c in range(0, n + 3):
    if c % i == 0 or c % j == 0:
        print(c, end=' ')
"""
cont = -1
sequencia = []
num = int(input('Informe quantos múltiplos deseja ver na sequência:'))
i = int(input('Informe um número, inteiro e positivo,usado como múltiplo da sequência:'))
j = int(input('Informe outro número, inteiro e positivo,usado como múltiplo da sequência:'))
while True:
    cont += 1
    multiploi = cont * i
    multiploj = cont * j
    if (multiploi == multiploj):
        if (multiploi not in sequencia):
            sequencia.append(multiploi)
    else:
        if (len(sequencia) == num - 1):
            if (multiploi > multiploj):
                if (multiploj not in sequencia):
                    sequencia.append(multiploj)
                else:
                    if (multiploi not in sequencia):
                        sequencia.append(multiploi)
        else:
            if (multiploi not in sequencia):
                    sequencia.append(multiploi)
            if (multiploj not in sequencia):
                    sequencia.append(multiploj)
        if (len(sequencia) >= num):
            sequencia.sort()
            for elemento in sequencia:
                print(elemento, end=' ')
            break
