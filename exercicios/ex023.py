# A solução Abaixo esta parcialmente errada
"""n1 = str(input('Digite um numero ate 9999: '))
n1 = n1.strip()
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(n1[3],n1[2],n1[1],n1[0]))"""
# A solução abaixo esta errada.
"""n = int(input('Digite um número ate 9999:'))
print('Unidade: ',int((n/10 - int(n/10))*10))
print('Dezena: ',int((n - (int(n/100))*100)/10))
print('Centena: ',int(((n/1000) - int(n/1000))*10))
print('Milhar: ',int(n/1000))"""
# Solução do professor:
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
