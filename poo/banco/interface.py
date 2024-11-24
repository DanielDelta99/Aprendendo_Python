from poo.banco.cliente import *

def linha(tipo='-',tamanho=40):
    print(tipo*tamanho)


def cabecalho(msg=''):
    linha()
    print(f'{msg:^40}')
    linha()


def opcoes(msg,lista):
    if msg != '':
        cabecalho(msg)
    for i,l in enumerate(lista):
        print(f'[{i+1}] - {l}')
    while True:
        n = leiaint('Opção: ')
        if 0 < n < len(lista)+1:
            break
        else:
            print('\033[31mDigite uma opção valida.\033[m')
    linha()
    return n


def leianome(msg):
    while True:
        try:
            nome = str(input(msg)).strip().lower()
            divisao = nome.split()
            nome = ''.join(divisao)
            if nome == '':
                print('\033[31mO usuariu preferiu cancelar o cadastro.\033[m')
                return 'SAIR'
            elif nome.isalpha():
                nome = ' '.join(divisao)
                return nome.title()
            else:
                print('\033[31mERRO: Caracteres invalidos.\033[m')
        except:
            print('Erro no tratamento de str')




def leiaint(msg):
    while True:
        try:
            n = input(msg).strip()
            if n in '':
                n = 0
            return int(n)
        except KeyboardInterrupt:
            print('\n\033[32mO usuario preferiu cancelar a rotina\033[m')
            break
        except:
            print('\033[31mERRO: por favor, digite um número válido.\033[m')
        else:
            break


def leiafloat(msg):
    while True:
        try:
            n = input(msg).replace(',', '.').strip()
            if n in '':
                n = 0
            return float(n)
        except KeyboardInterrupt:
            print('\n\033[32mO usuario preferiu cancelar a rotina\033[m')
            break
        except:
            print('\033[31mERRO: por favor, digite um número válido\033[m')
        else:
            break


def cadastro(clientes):
    while True:
        try:
            valor1 = 0
            tipo = 'Poupança'
            cabecalho('CADASTRO DE CLIENTE')
            nome = leianome('Seu nome: ')
            if nome == 'SAIR':
                break
            #verificaçao de existencia
            if not nome in clientes:
                linha()
                n = opcoes('Tipo de conta:',['Corrente','Poupança'])
                if n == 1:
                    tipo = 'Corrente'
                    valor1 = float(50)
                elif n == 2:
                    tipo = 'Poupança'
                    valor1 = float(150)
                valor = leiafloat('Deposito inicial: R$ ') + valor1
                linha()
                n = opcoes('',['CONFIRMAR', 'CANCELAR'])
                if n == 1:
                    novo_cliente = Client(nome, tipo, valor,True)
                    clientes[nome] = novo_cliente
                    print('\033[34mConta aberta com sucesso.\033[m')
                else:
                    print('\033[32mCadastro cancelado.\033[m')

            elif not clientes[nome].status:
                linha()
                clientes[nome].informacoes()
                n = opcoes('Deseja reativar a conta: ',['SIM', 'NÃO'])
                if n == 1:
                    clientes[nome].reativar_conta()
            else:
                print('\033[31mEsse cliente já existe em nosso banco de dados.\033[m')
        except:
            print('Erro def cadastro')
        else:
            return clientes
            break



def login(clientes):
    while True:
        try:
            cabecalho('LOGIN CLIENTE')
            nome = leianome('Seu nome de login: ')
            if not nome in clientes:
                print('Cliente não encontrado...')
            elif clientes[nome].status:
                cliente = clientes[nome]
                linha()
                cliente.informacoes()
                linha()
                conta(cliente)
                clientes[nome] = cliente

            elif not clientes[nome].status:
                linha()
                clientes[nome].informacoes()
                linha()
                n = opcoes('Deseja reativar a conta: ',['SIM', 'NÃO'])
                if n == 1:
                    clientes[nome].reativar_conta()
        except:
            print('Erro de def login')
        else:
            return clientes
            break


def conta(cliente):
    try:
        while True:
            n = opcoes('',['SACAR','DEPOSITAR','INATIVAR CONTA','SAIR'])
            if n == 1:
                nn = leiafloat('Valor a sacar: ')
                cliente.sacar(nn)
                linha()
            elif n == 2:
                nn = leiafloat('Valor a depositar: ')
                cliente.deposito(nn)
                linha()
            elif n == 3:
                inativar_conta(cliente)
                break
            elif n == 4:
                break
    except:
        print('Erro def conta')

def inativar_conta(cliente):
    try:
        cabecalho('INATIVAR CONTA CLIENTE')
        while cliente.saldo > 0:
            n = leiafloat('Primeiro saque seu dinheiro: ')
            cliente.sacar(n)
        n = opcoes('Vai mesmo inativar a conta: ',['CONFIRMAR','SAIR'])
        if n == 1:
            cliente.inativar_conta()
    except:
        print('Erro de def inativar_cota')