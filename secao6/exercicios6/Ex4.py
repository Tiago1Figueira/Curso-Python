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
"""
for mil in range(0, 100_001):
    if mil % 1000 == 0:
        print(mil)



