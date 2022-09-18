"""
#1
for i in range(3,18,3)
    print(i)

#2
print('=' * 55, 'OS MÚLTIPLOS DE 3 SÃO:', '='*65)
for i in range(1, 18):
    if i % 3 == 0:
        print(i, end=' ')

#3
for i in range(1, 18):
    if i % 3 == 0 :
        print(i, end=' ')
        print('\n')
#4
for i in range(3, 18, 3):
    print(i, end=' ')

#5
#5
for i in range(3,18,3):
    print(i,end=' ')
"""
print('%' * 50, 'MOSTRA OS 5 PRIMEIROS MÚLTIPLOS 3 NUM RANGE:', '%' * 50)
for i in range(1, 16):
    if i % 3 == 0:
        print(i)
