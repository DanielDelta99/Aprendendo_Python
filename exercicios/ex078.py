lista = list()
for n in range(0,5):
    lista.append(int(input(f'Gaveta {n} recebe: ')))
print(f'você digitou {lista}')
maior = max(lista)
menor = min(lista)
print(f'O maior número é {maior} e aparece nas posições ',end='')
for i,n in enumerate(lista):
    if n == maior:
        print(i,end='... ')
print()
print(f'O menor número é {menor} e aparece nas posições ',end='')
for i,n in enumerate(lista):
    if n == menor:
        print(i,end='... ')