lista = []
c = 0
fim = int(input('Quantos valores que você que adicionar? '))
while True:
    while True:
        lista.insert(c,int(input(f'N{c}: '))) # n = int(input('Add'))
        if lista.count(lista[c]) > 1:         # if n not in lista:
            lista.pop()                           # lista.append(n)
            print('O numero já existe')
        else:
            break
    c += 1
    if c == fim:
        break
lista.sort()
print(lista)