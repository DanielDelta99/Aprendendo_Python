def fmoedas(num=0):
    return f'R$ {num:.2f}'.replace('.',',')

def metade(num=0,fmoeda=False):
    num = num/2
    # return num if fmoeda is False else fmoedas(num)
    # return num if not fmoeda else fmoedas(num)
    if fmoeda:
        return fmoedas(num)
    else:
        return num

def dobro(num=0,fmoeda=False):
    num = num*2
    if fmoeda:
        return fmoedas(num)
    else:
        return num

def almentando(num=0,p=0,fmoeda=False):
    num = num + (num*p/100)
    if fmoeda:
        return fmoedas(num)
    else:
        return num

def diminuindo(num=0,p=0,fmoeda=False):
    num = num - (num*p/100)
    if fmoeda:
        return fmoedas(num)
    else:
        return num

