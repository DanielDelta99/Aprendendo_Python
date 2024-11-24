lista = []
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    lista.append(n)
print(f'Foram digitados {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Lista em ordem decrecente {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista e esta na {lista.index(5)} posição')
else:
    print('O valor 5 não faz parte da lista')