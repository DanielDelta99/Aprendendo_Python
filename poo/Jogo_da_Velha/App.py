from poo.Jogo_da_Velha.System_Game import Velha
from poo.Jogo_da_Velha.Player import Jogador

j1 = Jogador('Daniel')
j2 = Jogador('Amanda')
partida = Velha()

while True:
    partida.iface()
    if partida.jogadas % 2 == 0:
        wins = partida.jogada(j1)
        if wins:
            break
    else:
        wins = partida.jogada(j2)
        if wins:
            break
    if partida.jogadas == 9:
        partida.iface()
        print('!!!Deu velha!!!')
        break
