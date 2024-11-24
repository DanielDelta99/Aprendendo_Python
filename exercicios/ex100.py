#Um projeto que customizei os retornos com sleeps e com um print inteligente de soma.
from time import sleep
from random import randint

lista = []

def sorteio(n):
    frase = ('Sorteando os valores da lista: ')
    for i in range(0, len(frase)):
        print(frase[i], end='')
        sleep(0.1)
    for m in range(0,5):
        n.append(randint(1,10))
        print(n[m],end=' ')
        sleep(0.5)
    print('Pronto!!!')

def somapar(n):
    frase = (f'Somando os valores pares da lista {n}: ')
    for i in range(0,len(frase)):
        print(frase[i],end='')
        sleep(0.1)
    primeiro = True
    par = 0
    for i in range(0,len(n)):
        if n[i] % 2 == 0:
            sleep(0.5)
            print(n[i],end=' ')
            par += n[i]
            primeiro = False
        if i < len(n)-1 and n[i+1] % 2 == 0 and primeiro == False:
            sleep(0.5)
            print('+',end=' ')
    sleep(0.5)
    print(f'= {par}')

def carregando():
    for n in range(0,55):
        print('-',end='')
        sleep(0.05)
    print()

sorteio(lista)
carregando()
somapar(lista)