# Forma do professor
from time import sleep
def contador(a,b,c):
    if c == 0:
        c = 1
    if c < 0:
        c = -c
    print('-=' * 30)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a > b:
        while a >= b:
            print(a, end=' ')
            a -= c
            sleep(0.25)
        print('FIM')
    else:
        while a <= b:
            print(a, end=' ')
            a += c
            sleep(0.25)
        print('FIM')


contador(0,10,1)
contador(10,0,2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('passo: '))
contador(a,b,c)
