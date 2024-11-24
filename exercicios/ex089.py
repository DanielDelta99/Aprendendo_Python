#Antes da correçao
lista = []
nome = []
notas = []
while True:
    n = str(input('Nome: '))
    if n.upper() == 'FIM':
        break
    nome.append(n)
    notas.append(int(input('Nota 01: ')))
    notas.append(int(input('Nota 02: ')))
    nome.append(notas[:])
    nome.append((notas[0]+notas[1])/2)
    lista.append(nome[:])
    nome.clear()
    notas.clear()
print(f'{'No. '}{'NOME':<10}{'MÉDIA'}')
print('-'*20)
for i,n in enumerate(lista):
    print(f'{i:<4}{n[0]:<10}{n[2]:.1f}')
while True:
    print('-'*40)
    i = int(input('Mostrar notas do aluno? '))
    if i == 999:
        break
    elif -1 < i < len(lista):
        print(f'As notas de {lista[i][0]} são {lista[i][1]}')
    else:
        print('Aluno não cadastrado')
print('Fim do programa!!!')
