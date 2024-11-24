# apos ver a aula 21 voltei para fazer algumas correçoes
from time import sleep
from random import randint

lista = []

def maior(n):
    print('-'*40)
    print('Analizando os valores passados...')
    for i in n:
        print(i,end=' ')
        sleep(0.25)
    print(f'Foram informados {len(n)} valores ao todo.')
    print(f'O maior valor informado foi {max(n)}.')


for i in range(0,6):
    lista.append(randint(1,10))
maior(lista)
lista.clear()
k = 4
for j in range(0,4):
    k -= 1
    for i in range(0,k):
        lista.append(randint(1,10))
    if len(lista) == 0:
        print('-' * 40)
        print('Analizando os valores passados...')
        print('''Foram informados 0 valores ao todo.\nO maior valor informado foi 0. ''')
    else:
        maior(lista)
        lista.clear()
