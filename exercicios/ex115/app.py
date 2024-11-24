from util import systen,dado

lista = []

while True:
    n = systen.menu()
    if n == 1:
        systen.cadastradas(lista)
    elif n == 2:
        lista.append(systen.cadastro())
    elif n == 3:
        dado.txt(f'{'Saindo do sistema...':^47}','-')
        break

