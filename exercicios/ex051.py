n1 = int(input('1° Número: '))
n2 = int(input('2° Número: '))
#minha resolução
passo = n2 - n1
for c in range(1,11):
    print(n1,end=' ')
    n1 += passo
#Resolução do professor
n10 = n1 + (10 - 1) * n2
for c in range(n1,n10+n2,n2):
    print(c,end=' ')