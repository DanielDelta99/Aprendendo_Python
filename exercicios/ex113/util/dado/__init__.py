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