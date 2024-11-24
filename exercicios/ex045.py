from random import randint
from time import sleep
co = {1:'\033[31m',2:'\033[32m',3:'\033[33m',4:'\033[34m',5:'\033[m'}# lista de cores
lista = {1:'pedra',2:'Papel',3:'Tesoura'}#lista de itens de game
load = 'JOKENPÔ:'#lista de palavra
c = randint(1,3)#sorteio de jogada cpu

print('{:=^40}'.format(' \033[31mJOKENPÔ\033[m '))#cabeçalho
p = int(input('''[1] pedra \n[2] Papel \n[3] Tesoura\nSua escolha? '''))#Entrada de dados player
print('='*32)
#Carregamento
for j in range(0,8):
    print(load[j],end= ' ')
    sleep(0.3)
#Comparador de dados
if 1 <= p <= 3:
    if p == c:
        print('{}EMPATE{}'.format(co[2],co[5]))
    elif p == 1 and c == 3 or p == 2 and c == 1 or p == 3 and c == 2:
        print('\033[34mPLAYER VENCEU\033[m')
    else:
        print('\033[31mCPU VENCEU\033[m')
    print('='*32)
    sleep(0.3)
    print('O Computador escolheu \033[31m{}\033[m \nVocê escolheu \033[34m{}\033[m'.format(lista[c],lista[p]))
else:
    print('OPÇÃO INVALIDA!!!')