from exercicios.ex115.util import dado

def menu():
    print('''-----------------------------------------------
                MENU PRINCIPAL
-----------------------------------------------
\033[33m1\033[m - \033[34mVer pessosa cadastradas\033[m
\033[33m2\033[m - \033[34mCadastrar pessoas\033[m
\033[33m3\033[m - \033[34mSair do programa\033[m
-----------------------------------------------''')
    while True:
        op = dado.leiaint('\033[33mSua opção: \033[m')
        if op > 3 or op < 1:
            print('\033[31mOpção invalida\033[m')
        else:
            return op
            break

def cadastradas(lista):
    print('-'*47)
    print(f'{'PESSOAS CADASTRADAS':^47}')
    print('-' * 47)
    for dc in lista:
        print(f'{dc['nome']:30}{dc['idade']} anos')


def cadastro():
    print('-' * 47)
    print(f'{'CADASTRO DE PESSOAS':^47}')
    print('-' * 47)
    dc = {}
    lista = []
    dc['nome'] = str(input('Nome: '))
    dc['idade'] = dado.leiaint('Idade: ')
    dado.txt(f'\033[34mCadastro de {dc['nome']} adicionado com sucesso.\033[m')
    return dc