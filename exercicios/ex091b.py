# Forma do professor
from random import randint
from operator import itemgetter
from time import sleep
dados02 = []
dados = {'Jogador 01': randint(1,6),
'Jogador 02': randint(1,6),
'Jogador 03': randint(1,6),
'Jogador 04': randint(1,6),
}
for i, j in dados.items():
    print(f'{i} tirou {j}')
    sleep(0.5)
print('===== Ranking =====')
dados02 = sorted(dados.items(), key=itemgetter(1), reverse=True)
c = 0
for i in dados02:
    c += 1
    print(f'{c}° lugar: {i[0]} com {i[1]}')
    sleep(0.5)
