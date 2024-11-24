from random import randint
from time import sleep
lista = []
sorte = []
print(f'''{'':-^35}
{'JOGO NA MEGA CENA':^35}
{'':-^35} ''')
jogos = int(input('Quantos jogos? '))
print(f'{'':-^35} ''')
for c in range(0,jogos):
    for i in range(0,6):
        while True:
            n = randint(1,60)
            if n not in sorte:
                break
        sorte.append(n)
        sorte.sort()
    lista.append(sorte[:])
    sorte.clear()
for i,n in enumerate(lista):
    sleep(0.5)
    print(f'jogo {i+1:2}: {n}')
