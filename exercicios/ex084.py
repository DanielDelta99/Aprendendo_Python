# listas compostas
lista = []
dados = []
peso = peso1 = 0
while True:
    dados.append(str(input('Nome: ')))
    if 'FIM' in dados[0].upper():
        break
    dados.append(int(input('Peso Kg: ')))
    if dados[1] > peso:
        peso = dados[1]
    if dados[1] < peso1 or peso1 ==0:
        peso1 = dados[1]
    lista.append(dados[:])
    dados.clear()
print(f'Ao todo {len(lista)} pessoas foram cadastras.')
print(f'O maior peso foi {peso:.1f} Kg. peso de',end=' ')
for n in lista:
    if n[1] == peso:
        print(f'[{n[0]}]',end=' ')
print()
print(f'O menor peso foi {peso1:.1f} Kg. peso de',end=' ')
for n in lista:
    if n[1] == peso1:
        print(f'[{n[0]}]',end=' ')
