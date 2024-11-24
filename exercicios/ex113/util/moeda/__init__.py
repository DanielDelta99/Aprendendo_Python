def fmoedas(num=0):
    return f'R$ {num:.2f}'.replace('.',',')

def metade(num=0,fmoeda=False):
    num = num/2
    # return num if fmoeda is False else fmoedas(num)
    return num if not fmoeda else fmoedas(num)

def dobro(num=0,fmoeda=False):
    num = num*2
    return num if not fmoeda else fmoedas(num)

def almentando(num=0,p=0,fmoeda=False):
    num = num + (num*p/100)
    return num if not fmoeda else fmoedas(num)

def diminuindo(num=0,p=0,fmoeda=False):
    num = num - (num*p/100)
    return num if not fmoeda else fmoedas(num)

def resumo(num,pmax,pmen):
    print (f'''
------------------------------------- 
           RESUMO DO VALOR
-------------------------------------
{f'Preço analisado:':20} R$ {fmoedas(num)}
{f'Dobro do preço:':20} R$ {dobro(num,True)}
{f'Metade do preço:':20} R$ {metade(num,True)}
{f'{pmax}% de aumento:':20} R$ {almentando(num,pmax,True)}
{f'{pmen}% de redução:':20} R$ {diminuindo(num,pmen,True)}
-------------------------------------''')