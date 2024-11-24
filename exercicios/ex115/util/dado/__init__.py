def leiadin(msg):

    while True:
        numero = True
        nu = input(msg).strip()

        num = nu.replace(',', '.')
        if num.count('.') >= 2:
            numero = False
        if num.count('.') == 1 and len(num) == 1:
            numero = False
        num = num.replace('.','0')
        if num.isnumeric() == False:
            numero = False

        if numero == False:
            print(f'\033[31mERRO: "{nu}" é um preço inválido!\033[m')
        else:
            nu = num.replace(',','.').strip()
            return float(num)
            break


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
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
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
            print('\033[31mERRO: por favor, digite um número real válido\033[m')
        else:
            break


def txt(msg,linhas='',tamanho=0,velocidade=0.05,end=False):
    """
    ==> txt é uma função que trabalha com a visualização de textos.
    :param msg: Recebe a mensagem que sera exibida.
    :param linhas: (Padrao Vasio) - Defina o tipo de linha que sera exibida.
    :param tamanho: (Padrao mesmo tamnho da msg) - Variação no comprimento da linha.
    :param velocidade: (padrao 0.05) - Velocidade do deley da exibição.
    :param end: (padrao desligado ) - Quer que contie na frente.
    :return: Não retorna valores.
    """
    from time import sleep
    texto = (msg)

    if tamanho == 0:
        tamanho = len(msg)

    if len(linhas) >= 1:
        print(f'{linhas}' * tamanho)
    for i in range(0, len(texto)):
        sleep(velocidade)
        print(texto[i], end='')
    if end == False:
        print()
    if len(linhas) >= 1:
        print(f'{linhas}' * tamanho)
