from time import sleep
frase = str(input('Digite um frase: ')).lower().split()
frase = ''.join(frase)
n = len(frase)
erro = 0
for c in range(0,n):
    n -= 1
    print(frase[n], end='')
    sleep(0.5)
    if frase[c] != frase[n]:
        erro = 1
if erro == 0:
    print('\nA frase é palíndromo')
else:
    print('\nA frase não é palíndromo')