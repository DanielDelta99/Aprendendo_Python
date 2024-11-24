from time import sleep
def contador(a,b,c):
    if a > b and c > 0:
        c = -c
    elif a < b and c < 0:
        c = -c
    elif c == 0 and a > b:
        c = -1
    elif c == 0 and a < b:
        c = 1

    print('-='*30)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    for n in range(a,b,c):
        print(n,end=' ')
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
