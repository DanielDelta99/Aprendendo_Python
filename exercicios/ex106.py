
def ajuda():
    while True:
        print('-' * 32)
        txt('    \033[32mSistema de ajuda pyHelp\033[m    ')
        print('-' * 32)
        txt('Função ou Biblioteca: ',end=True)
        msg = str(input())
        if msg.upper().strip() in 'SAIR,EXIT,FIM':
            txt('\033[32mAté logo meu amigo!!!\033[m',linhas=True)
            break
        txt(f'\033[34mAcesando o manual do comando\033[m \033[31m{msg}\033[m',linhas=True,tamanho=-16)
        help(msg)

def txt(msg,linhas=False,tamanho=0,velocidade=0.05,end=False):
    """
    ==> txt é uma função que trabalha com a visualização de textos.
    :param msg: Recebe a mensagem que sera exibida.
    :param linhas: (Padrao desligado) - Exibição de linhas na parte de baixo e cima do texto.
    :param tamanho: (Padrao mesmo tamnho da msg) - Variação no comprimento da linha.
    :param velocidade: (padrao 0.05) - Velocidade do deley da exibição.
    :param end: (padrao desligado ) - Quer que contie na frente.
    :return: Não retorna valores.
    """
    from time import sleep
    texto = (msg)

    if linhas:
        print('-' * (len(texto) + tamanho))
    for i in range(0, len(texto)):
        sleep(velocidade)
        print(texto[i], end='')
    if end == False:
        print()
    if linhas:
        print('-' * (len(texto) + tamanho))

ajuda()
