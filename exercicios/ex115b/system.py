from time import sleep

from exercicios.ex115b.lib.arquivo import *
from exercicios.ex115b.lib.interface import *

arq = 'save115.txt'
if not ArquivoExiste(arq):
     CriarArquivo(arq)

while True:
    op = menu(['Ver pessosa cadastradas','Cadastrar pessoas','Sair do programa'])
    if op == 1:
        sleep(0.5)
        cabeçalho('PESSOAS CADASTRADAS')
        LerArquivo(arq)
    elif op == 2:
        sleep(0.5)
        cabeçalho('CADASTRO DE PESSOAS')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        EscreverArquivo(arq,nome,idade)
    elif op == 3:
        txt(f'{'Saindo do sistema...':^47}', '-')
        break
