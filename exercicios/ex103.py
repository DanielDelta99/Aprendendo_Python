def ficha(nome = '',gols = 0):
    if nome == '':
        nome = 'Desconhecido'
    if gols.isnumeric() != True:
        gols = 0
    return(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


frase = ficha(input('Nome: ').strip(),(input('Gols: ')))
print(frase)
