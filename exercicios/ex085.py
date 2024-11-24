lista = [[],[]]
for c in range(0,7):
    n = int(input(f'Digite {c+1}° número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Números impares: {lista[1]}\nNúmeros pares: {lista[0]}')
