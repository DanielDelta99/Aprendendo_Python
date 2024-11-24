# Refazer exercicio
n1 = float(input('Valor a se converter m: '))
print('A medida de {}m corresponde a\n{} km\n{} hm\n{} dam\n{:.0f} dm\n{:.0f} cm\n{:.0f} mm'.format(n1,(n1/1000),(n1/100),(n1/10),(n1*10),(n1*100),(n1*1000)))