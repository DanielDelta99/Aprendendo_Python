from datetime import date
ano = date.today().year
maior = 0
menor = 0
for n in range(1,8):
    n1 = int(input('{}° Data de nascimento: '.format(n)))
    idade = ano - n1
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('Das pessoas cadastradas {} são menores e {} são maiores de 18 anos.'.format(menor,maior))