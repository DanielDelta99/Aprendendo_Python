soma = 0
cont = 0
for c in range(1,7):
    n = int(input('{}° Número: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('{} números pares com a soma de {}'.format(cont,soma))
