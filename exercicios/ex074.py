from random import choice,randint
numeros = (1,2,3,4,5,6,7,8,9,10)
gg = pp = 0
for c in range(0,5):
    n = choice(numeros)
    print(n,end=' ')
    if n > gg:
       gg = n
    if n < pp or pp == 0:
        pp = n
print()
print(f'O maior número foi {gg}\nE o menor número foi {pp}')

#Resposta correta
numero = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
for n in numero:
    print(n,end=' ')
print(f'\n{max(numero)}')
print(min(numero))