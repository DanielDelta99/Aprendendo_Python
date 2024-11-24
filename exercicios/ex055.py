maior = 0
menor = 0
for n in range(1,6):
    n1 = float(input('{}° Peso Kg: '.format(n)))
    if n1 > maior:
        maior = n1
    if n1 < menor or menor == 0:
        menor = n1
print('Menor peso: {:.1f} Kg \nMaior peso:  {:.1f} Kg '.format(menor,maior))