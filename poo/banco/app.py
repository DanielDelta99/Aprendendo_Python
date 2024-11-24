from poo.banco.arquivo import *
from poo.banco.interface import *
from poo.banco.cliente import *
import pickle

arq = 'C:/Users/Daniel/Documents/GitHub/Aprendendo_Python/poo/banco/arquivo/clientes.pickle'
if not arquivo_existe(arq):
    criar_arquivo(arq)
clientes = carregar_clientes(arq)

while True:
    n = opcoes('BANCO DELTA',['CADASTRO', 'LOGIN','SAIR'])
    if n == 1:
        clientes = cadastro(clientes)
    elif n == 2:
        clientes = login(clientes)
    elif n == 3:
        salvar_clientes(clientes,arq)
        break
