n1 = int(input('Número de inicio da PA: '))
n2 = int(input('Razão da PA: '))
c = 0
pa = n1
termos = 0
fim = 10
while fim != 0:
    c = fim
    while c != 0:
        termos += 1
        c -= 1
        print('{}..'.format(pa), end=' ')
        pa += n2
    print('')
    fim = int(input('Mais quantos termos? '))
print('Progressão finalizada com {} termos mostrados.'.format(termos))

