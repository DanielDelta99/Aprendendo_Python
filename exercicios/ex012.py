n1 = float(input('Preço do produto R$: '))
n2 = n1*5/100
print('Seu desconto será de R$ {:.2f},900 logo o preço atualizado do produto é de R$ {:.2f}'.format(n2,n1-n2))