class Jogador:
    idd = 0
    def __init__(self,nome):
        if Jogador.idd == 0:
            self._nome = f'\033[31m{nome}\033[m'
            self._simbulo = '\033[31mX\033[m'
        else:
            self._nome = f'\033[34m{nome}\033[m'
            self._simbulo = '\033[34mO\033[m'
        Jogador.idd += 1


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome


    @property
    def simbolo(self):
        return self._simbulo

    @simbolo.setter
    def simbulo(self,n):
        self._simbulo = n