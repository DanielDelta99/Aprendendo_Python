lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    lista.append(n)
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f'Lista geral {lista}')
print(f'Lista impar {impares}')
print(f'Lista pares {pares}')
