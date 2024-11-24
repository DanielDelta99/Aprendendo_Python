from random import randint
n = randint(0,5)
if n < 3:
    print('A01')
    if n == 2:
        print('X=X')
elif n == 3:
    print('A02')
elif n in (4, 5):
    print('SS99')
print(n)