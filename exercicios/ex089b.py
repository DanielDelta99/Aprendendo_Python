#Apos a correção
lista = []
while True:
    nome = str(input('Nome: '))
    if nome.upper() == 'FIM':
        break
    nota1 = int(input('Nota 01: '))
    nota2 = int(input('Nota 02: '))
    media = (nota2 + nota1)/2
    lista.append([nome,[nota1, nota2],media])
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
