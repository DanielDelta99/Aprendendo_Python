from datetime import date
from time import sleep
nome = str(input('Digite seu primeiro nome: '))
sexo = str(input('Qual é seu genero [M/F]: '))
n = int(input('Digite sua data de nascimento: '))
print('\033[34mCARREGANDO...\033[m')
sleep(3)
anoatual = date.today().year
idade = anoatual - n
if sexo == 'M':
    if idade < 18:
        saldo = 18 - idade
        print('{}, como você tem apenas \033[32m{} anos\033[m, Faltam \033[32m{} anos\033[m para se alistar.'.format(nome,idade,saldo))
        print('O ano do seu alistamento será em {}'.format(anoatual + saldo))
    elif idade > 18:
        saldo = idade - 18
        print('{} você Já tem \033[31m{} anos?\033[m Deveria ter se alistado há \033[31m{} anos\033[m.'.format(nome,idade,saldo))
        print('O ano do seu alistamento foi em {}'.format(anoatual - saldo))
    else:
        print('{}, como você tem \033[34m{} anos\033[m, estao já está na hora de se alistar.'.format(nome,idade))
        print('Esse é o ano {}'.format(anoatual))
else:
    print('{}, por ser mulher, você não é obrigada a se alistar.'.format(nome))