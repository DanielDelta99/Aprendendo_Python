player = {}
gols = []
jogadores = []
# Leitura
while True:
    gols.clear()
    player.clear()
    print('='*36)
    nome = str(input('Nome do jogador: ')).strip()
    if nome.upper() in 'FIM':
        break
    player['Nome'] = nome
    n = int(input(f'Quantas partidas {player['Nome']} jogou: '))
    total = 0
    for i in range(0,n):
        gols.append(int(input(f'   Quantos gols na {i+1}° partida: ')))
        total += gols[i]
    player['Gols'] = gols[:]
    player['Total'] = total # player['Total'] = sum(gols)
    jogadores.append(player.copy())
# Tabela
print('-='*17)
print(f'{'Cod':} {'Nome':15}{'Total'} {'Gols'}')
print('='*36)
for i,j in enumerate(jogadores):
    print(f'{i:3} {j['Nome']:15}{j['Total']:<6}{j['Gols']:}')
print('='*36)
# Apuramento
while True:
    jog = int(input('Mostrar dados de qual jogador? '))
    if jog == 999:
        break
    elif jog >= len(jogadores) or jog < 0:
        print(f'Erro! não existe jogador com o codigo {jog}!, tente novamente.')
    else:
        print(f'--- Levantamento do jogador {jogadores[jog]['Nome']} ---')
        for i, j in enumerate(jogadores[jog]['Gols']):
            print(f'    => Na {i + 1}° partida, fez {j} gols.')
        print(f'foi um total de {jogadores[jog]['Total']} gols.')
        print('=' * 36)
