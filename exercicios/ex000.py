from random import randint
from time import sleep
lista = []
sorte = []
print(f'''{'':-^25}
{'JOGO NA MEGA CENA':^25}
{'':-^25} ''')
jogos = int(input('Quantos jogos? '))
for c in range(0,jogos):
    for i in range(0,6):
        while True:
            n = randint(1,60)
            if n not in sorte:
                break
        sorte.append(n)
    lista = sorte[:]
    sorte.clear()
sleep(0.5)
print(f'jogo: {lista}')