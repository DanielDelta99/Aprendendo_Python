from random import randint
n = int(input('Escolha um numero de 1 a 5: '))
n1 = randint(1,5)
if n > 5:
    print('NUMERO INVALIDO!!!')
else:
    if n == n1:
       print('PARABENS VOCE VENCEU!!!')
    else:
       print('VOCE PERDEU')
       print('O numero sorteado foi {}'.format(n1))
    print('END GAME')