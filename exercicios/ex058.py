from random import randint
from time import sleep
n = randint(0,10)
m = 11
c = 0
i = 0
v = 'PARABENS VOCÊ É UM !!!VIDENTE!!!'
print('\033[32m-------------------------- O VIDENTE ---------------------------\033[m')
print('Consegue adivinhar em que número que estou pensando? (0 a 10)')
while m != n:
    m = int(input(''))
    if 0 <= m <= 10:
       c +=  1
       if m < n:
           print('Mais')
       elif m > n:
           print('Menos')
    else:
        print('\033[31m!!!Jogada invalida!!!\033[m')
print('\033[32m-\033[m'*64)
if c == 1:
    for i in range(0,len(v)):
        sleep(0.2)
        print('{}{}{}'.format('\033[34m',v[i],'\033[m'),end= '')
    print('')
    print('Como advinhou que tinha pensado no número {}'.format(n))
else:
    print('Você acertou, mas precisou de \033[33m{}\033[m chances'.format(c))
    print('Eu realmente pensei no número {}'.format(n))