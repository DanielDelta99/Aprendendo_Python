media = 0
maior = 0
mulheres = 0
velho = ''
for n in range(1,5):
    print('{:-^20}'.format(' {}° Pessoa '.format(n)))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sex = str(input('Genero [M/F]: ')).strip().upper()
    media += idade
    if idade > maior and sex == 'M':
        maior = idade
        velho = nome
    if sex == 'F' and idade < 20:
        mulheres += 1
print('''Media de idade do grupo é de {:.1f} anos.
Nome do homem mais velho é {} a qual tem {} anos.
{} Mulheres tem idade menor que 20 anos.'''.format(media/4,velho,maior,mulheres))

