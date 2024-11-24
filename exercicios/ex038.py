n1 =  int(input('1° Número: '))
n2 = int(input('2° Número: '))
if n1 > n2:
    print('O \033[34m1°\033[m número é o maior.')
elif n1 < n2:
    print('O \033[35m2°\033[m número é o maior.')
else:
    print('Os dois números são iguais.')