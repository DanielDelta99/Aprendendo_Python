# Listas simples/ mudei para lista composta
lista = [[],[]]
nome = ''
c = 0
while True:
    nome = str(input('Nome: '))
    if 'FIM' in nome.upper():
        break
    lista[0].append(nome)
    lista[1].append(int(input('Peso Kg: ')))
print(f'Ao todo {len(lista[0])} pessoas foram cadastras.')
print(f'O maior peso foi {max(lista[1]):.1f} Kg. peso de',end=' ')
for i,j in enumerate(lista[1]):
    if lista[1][i] == max(lista[1]):
        print(lista[0][i],end=' ')
print()
print(f'O menor peso foi {min(lista[1]):.1f} Kg. peso de',end=' ')
for i,j in enumerate(lista[1]):
    if lista[1][i] == min(lista[1]):
        print(lista[0][i],end=' ')
