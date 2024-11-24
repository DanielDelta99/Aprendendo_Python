print('Vamos calcular a sua idade!')
n1 = int(input('Digite o ano em que estamos: '))
n2 = int(input('Digite o ano de seu nascimento: '))
s = n1-n2
print('Se você nasceu em {}, e estamos em {}, entao você tem {} anos de idade'.format(n2,n1,s))
print(type(s))