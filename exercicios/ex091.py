# sem usar a biblioteca operator
from random import randint
from time import sleep
dados = {}
dedos = {}
for n in range(0,4):
    dados[f'Jogador 0{n+1}'] = randint(1,6)
print('Valores sorteados:')
for n, m in dados.items():
    print(f'O {n} tirou {m}')
    sleep(0.5)
for c in range(0,len(dados)):
    m = a = 0
    for i, j in dados.items():
        if j > m:
            m = j
            a = i
    dedos[a] = m
    del dados[a]
print()
print('Ranking dos jogadores: ')
c = 0
for n, m in dedos.items():
    c += 1
    print(f'{c}° lugar: {n} com {m}')
    sleep(0.5)
