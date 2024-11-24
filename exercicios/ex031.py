n = float(input('Distacia do destino km: '))
if n <= 200:
    n1 = n * 0.5
else:
    n1 = n * 0.45
print('Valor da passagem: R$ {:.2f}'.format(n1))