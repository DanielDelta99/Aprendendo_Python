n  = float(input('Valor do produto R$: '))
n1 = int(input('''Condição do pagamento:
[1] Dinheiro ou cheque
[2] Cartão de credito 1x
[3] Cartão de credito 2x
[4] Cartão de credito 3x
Qual a opção? '''))
if n1 == 1:
    nf = n - n*10/100
    print('''Pagamento no dinheiro ou cheque.
Desconto de 10%: R$ {:.2f}
O produto passou de R$ {:.2f} para R$ {:.2f}'''.format(n-nf,n,nf))
elif n1 == 2:
    nf = n - n*5/100
    print('''Pagamento no cartão de credito avista. 
Desconto de 5%: R$ {:.2f}
O produto pasou de R$ {:.2f} para R$ {:.2f}'''.format(n-nf,n,nf))
elif n1 == 3:
    print('''Parcelamento em 2x sem juros
valor do produto: {:.2f}
2 parcelas de R$ {:.2f}'''.format(n,n/2))
elif n1 == 4:
    par = int(input('Quantas parcelas? '))
    nf = n + n*20/100
    print('''Parcelamento em {}x.
Juros de 20%: R$ {:.2f}
O produto passou de R$ {:.2f} para R$ \033[31m{:.2f}\033[m
{} parcelas de R$ {:.2f}'''.format(par,nf-n,n,nf,par,nf/par))
else:
    print('ERRO')