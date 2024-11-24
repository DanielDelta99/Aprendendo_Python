player = {}
gols = []
player['Nome'] = str(input('Nome do jogador: '))
n = int(input(f'Quantas partidas {player['Nome']} jogou: '))
total = 0
for i in range(0,n):
    gols.append(int(input(f'Quantos gols na {i+1}° partida: ')))
    total += gols[i]
player['gols'] = gols[:]
player['Total'] = total # player['Total'] = sum(gols)
print('-='*30)
print(player)
print('-='*30)
for i,j in player.items():
    print(f'O campo {i} tem o valor {j}')
print('-='*30)
print(f'O jogador {player['Nome']} jogou {len(gols)} partidas')
for i,j in enumerate(gols):
    print(f'    => Na {i+1}° partida, fez {j} gols.')
print(f'foi um total de {player['Total']} gols.')
