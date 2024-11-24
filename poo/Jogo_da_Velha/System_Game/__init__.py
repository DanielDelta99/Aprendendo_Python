from poo.Jogo_da_Velha.Config import cabeçalho

class Velha:
    jogadas = 0
    def __init__(self):
        self._iface = [['1','2','3'],['4','5','6'],['7','8','9']]


    def iface(self):
        cabeçalho('JOGO DA VELHA',30)
        for l in self._iface:
            print('+-----+-----+-----+')
            print(f'|  {l[0]}  |  {l[1]}  |  {l[2]}  |')
        print('+-----+-----+-----+')

    def escolha(self,num,jog):
        for l in self._iface:
            if num in l:
                i = l.index(num)
                l[i] = jog
                Velha.jogadas += 1
                return True
        print('\033[31mJogada invalida\033[m')
        return False


    def verificação(self):
        for l in self._iface:
            if l[0] == l[1] == l[2]:
                return True
        for n in range(0,3):
            if self._iface[0][n] == self._iface[1][n] == self._iface[2][n]:
                return True
        if self._iface[0][0] == self._iface[1][1] == self._iface[2][2]:
            return True
        if self._iface[0][2] == self._iface[1][1] == self._iface[2][0]:
            return True


    def jogada(self,jogador):
        while True:
            n = input(f'{jogador.nome} onde vai jogar o {jogador.simbolo}: ').strip()
            valido = self.escolha(str(n),jogador.simbulo)
            if valido:
                break
        wins = self.verificação()
        if wins:
            self.iface()
            print(f'{jogador.nome} \033[32mvenceu a partida\033[m')
            return True
