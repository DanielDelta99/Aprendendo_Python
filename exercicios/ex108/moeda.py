def metade(num):
    return num/2

def dobro(num):
    return num*2

def almentando(num,p):
    return num + (num*p/100)

def diminuindo(num,p):
    return num - (num*p/100)

def fmoeda(n):
    return f'R$ {n:.2f}'.replace('.',',')