n = float(input('Seu salário: R$'))
if n > 1250:
    n1 = n + (n*10/100)
else:
    n1 = n + (n*15/100)
print('Novo salário: R${:.2f}'.format(n1))