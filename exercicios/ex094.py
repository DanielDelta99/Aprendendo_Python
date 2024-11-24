dados = {}
lista = []
media = 0
while True:
    nome = str(input('Nome: '))
    if nome.upper() in 'FIM':
        break
    dados['Nome'] = nome
    while True:
        gene = str(input('Genero[M/F]: ')).upper().strip()[0]
        if gene in 'MF':
            break
        else:
            print('Digite apenas M ou F')
    dados['Genero'] = gene
    dados['Idade'] = int(input('Idade: '))
    media += dados['Idade']
    lista.append(dados.copy())
media = media/len(lista)
print(f'''- O grupo tem {len(lista)} pessoas.
- A media de idade é de {media:.1f}
- As mulheres cadastradas foram: ''',end='')
for l in lista:
    if l['Genero'] == 'F':
        print(l['Nome'],end=' ')
print('\n- lista das pessoas que estão acima da média:'
      '')
for l in lista:
    if l['Idade'] > media:
        for i,j in l.items():
            print(f'{i} = {j};',end=' ')
        print()
