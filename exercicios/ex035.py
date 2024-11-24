n1 = int(input('1° Lado: '))
n2 = int(input('2° Lado: '))
n3 = int(input('3° Lado: '))
if n1 + n2 > n3 and n2 + n3 > n1 and n3 + n1 > n2:
    print('Pode formar um triangulo')
else:
    print('Não pode formar um triangulo')
