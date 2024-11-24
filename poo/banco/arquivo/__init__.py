import pickle
from poo.banco.interface import *

def arquivo_existe(doc):
    try:
        t = open(doc,'rt')
    except FileNotFoundError:
        return False
    else:
        t.close()
        return True


def criar_arquivo(doc):
    try:
        t = open(doc,'wt+')
    except:
        print('Erro ao tentar criar arquivo')
    else:
        t.close()


def carregar_clientes(arquivo):
    try:
        with open(arquivo, 'rb') as arq:
            return pickle.load(arq)  # Carregar o dicionário de clientes
    except (EOFError, FileNotFoundError):
        return {}  # Retorna um dicionário vazio se o arquivo estiver vazio ou corrompido


def salvar_clientes(clientes, arquivo):
    with open(arquivo, 'wb') as arq:
        pickle.dump(clientes, arq)

