n = int(input('Digite um número: '))
primo = 0
for c in range(1,n+1):
    if n % c == 0:
        primo += 1
if primo == 2:
    print('{} é um número primo'.format(n))
else:
    print('{} não é um número primo'.format(n))
