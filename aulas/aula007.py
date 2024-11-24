n1 = int(input('Escreva um numero:' ))
n2 = int(input('Escreva outro numero: '))
som = n1 + n2
sub = n1 - n2
div = n1 / n2
mul = n1 * n2
esp = n1 ** n2
div2 = n1 // n2
res = n1 % n2
print('A soma é {}, a subtração é {:.3f}, a divisão é {:.3f}, a multiplicação é {:.3f},'.format(som,sub,div,mul),end=' ')
print('a esponiciação é {:.3f}, a divisão inteira é {}, e a sobra dessa divisão é {}'.format(esp,div2,res))