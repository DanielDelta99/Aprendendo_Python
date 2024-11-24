n = ''
while 'M' != n != 'F':#poderia ter usado not in 'MmFf'
    n = str(input('Genero [M/F]: ')).upper().strip()
    if 'M' != n != 'F':
        print('Opção invalida!!!')
    else:
        print('Dados coletados com sucesso.')
print('Passou')