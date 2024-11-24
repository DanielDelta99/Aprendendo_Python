#Calculo de fatorial usando estrutura de repetição com teste logico.
n = int(input('Informe um número: '))
contador = n
mult = 1
print('{}! = '.format(n,n),end='')
while contador != 0:
    print('{}'.format(contador), end='')
    print(' X ' if contador > 1 else ' = ', end='')
    mult *= contador
    contador -= 1
print('{}'.format(mult))

#Calculo de fatorial usando estrutura de repetição com variavel de controle.
n = int(input('Informe um número: '))
contador = 0
mult = n
print('{}! = {}'.format(n,n),end=' ')
for contador in range(n-1,0,-1):
    print('X {}'.format(contador), end=' ')
    mult *= contador
print('= {}'.format(mult))