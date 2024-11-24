dic = {}
dic['nome'] = str(input('Nome: '))
dic['media'] = float(input('Media: '))
if dic['media'] < 6:
    dic['situacao'] = 'Reprovado!!!'
else:
    dic['situacao'] = 'Aprovado!!!'
print(f'O Aluno(a) {dic['nome']} está com a media de {dic['media']} e sua situaçao é {dic['situacao']}')