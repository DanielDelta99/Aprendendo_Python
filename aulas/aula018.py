lista = [['Daniel',26],['Amanda',23],['Nael',24],['Raquel', 22]]
i = 0
j = 0
for n in lista:
    for c in lista[i][:]:
        if j % 2 == 0:
            print(f'Nome: {c:.<20}',end = ' ')
        else:
            print(f'Idade: {c}')
        j += 1
    i += 1

for n in lista:
    print(f'{n[0]} Tem {n[1]} anos de idade')