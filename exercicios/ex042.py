n1 = int(input('1° Lado: '))
n2 = int(input('2° Lado: '))
n3 = int(input('3° Lado: '))
if n1 + n2 > n3 and n2 + n3 > n1 and n3 + n1 > n2:
    print('Pode formar um triângulo',end=' ')
    if n1 == n2 == n3:
        print('\033[34mequilátero\033[m')
    elif n1 == n2 or n2 == n3 or n3 == n1:
        print('\033[34misósceles\033[m')
    else:
        print('\033[34mescaleno\033[m')
else:
    print('\033[31mNão\033[m pode formar um triângulo')