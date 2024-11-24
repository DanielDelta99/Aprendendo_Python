from datetime import date
n = int(input('Ano de nascimento: '))
idade = date.today().year - n
print('Idade: {} \nSua categoria é:'.format(idade),end=' ')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SENIOR')
else:
    print('MASTER')
