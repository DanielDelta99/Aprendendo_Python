from poo.banco.interface import *

class Client:
    def __init__(self,cliente='Desconhecido',tipo='Poupança',saldo=0,status=False):
        self._cliente = cliente
        self._tipo = tipo
        self._saldo = saldo
        self._status = status

    @property
    def cliente(self):
        return self._cliente


    @cliente.setter
    def cliente(self,nome):
        self._cliente = nome

    @property
    def tipo(self):
        return self._tipo


    @tipo.setter
    def tipo(self,valor):
        self._tipo = valor


    @property
    def saldo(self):
        return self._saldo


    @saldo.setter
    def saldo(self,valor):
        self._saldo = valor


    @property
    def status(self):
        return self._status


    @status.setter
    def status(self,valor):
        self._status = valor


    def criar_conta(self,clientes):
        pass

    def inativar_conta(self):
        self._status = False
        print('Conta inativada com sucesso')


    def reativar_conta(self):
        self._status = True
        print('Conta reativada com sucesso')


    def sacar(self,valor):
        if not valor > self._saldo:
            self._saldo -= valor
        else:
            print('Saldo insuficiente')
        print(f'Saldo: R$ {self.saldo}')


    def deposito(self,valor):
        self._saldo += valor
        print(f'Saldo: R$ {self.saldo}')

    def informacoes(self):
        print('RESUMO:')
        print(f'{'Nome do cliente:':20} {self.cliente}')
        print(f'{'Tipo de conta:':20} {self.tipo}')
        if self._status:
            print(f'{'Status da conta:':20} Ativa')
        else:
            print(f'{'Status da conta:':20} Inativa')
        print(f'{'Saldo da conta:':20} R$ {self.saldo:.2f}')


