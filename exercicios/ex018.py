# Faltou converter os graus, pois o valor convertido é em radianos.
from math import sin,cos,tan, radians
n1 = int(input('Digite um angolo :°'))
print('Seno = {:.4f} \nCoseno = {:.4f} \nTangente = {:.4f}'.format(sin(radians(n1)),cos(radians(n1)),tan(radians(n1))))

