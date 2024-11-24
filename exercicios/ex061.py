n1 = int(input('Número de inicio da PA: '))
n2 = int(input('Razão da PA: '))
c = 10
pa = n1
while c != 0:
    c -= 1
    print('{}..'.format(pa), end=' ')
    pa += n2
print('Fim')