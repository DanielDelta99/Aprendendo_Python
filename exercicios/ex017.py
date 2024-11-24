import math
n1 = float(input('Cateto oposto: '))
n2 = float(input('Cateto adjacente: '))
# h = math.sqrt((math.pow(n1,2)) + (math.pow(n2,2)))
h = math.hypot(n1,n2)
print('A hipotenuza é {:.2f2}'.format(h))