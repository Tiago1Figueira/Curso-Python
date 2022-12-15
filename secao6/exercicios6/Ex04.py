"""
#1
for i in range(0, 101000, 1000):
    print(i)

#2
for i in range(0, 101000, 1000):
    print(i, end=' ')

#3
for i in range(0,101_000,1000):
    print(i)

for mil in range(0, 100_001):
    if mil % 1000 == 0:
        print(mil)
"""
print("*" * 50, 'MOSTRA OS VALORES INICIADOS EM 0 DE 1000 EM 1000 ATÉ 100_000', "*" * 50)
for i in range(0, 100_001, 1000):
    print(i)


