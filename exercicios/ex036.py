from time import sleep
#Cabeçalho
print('\033[33m=\033[m'*35)
q = 'BANCO DO POVO'
print('\033[31m{:=^35}\033[m'.format(q))
print('\033[33m=\033[m'*35)
#Entrada de dados
n = float(input('Valor do imprestimo: R$ '))
n1 = float(input('Salario: R$ '))
n2 = int(input('Em quantos anos deseja pagar: '))
p = n / (n2 * 12)
m = n1 * 30/100
#Condiçoes
print('\033[34mCARREGANDO...\033[m')
sleep(3)
if p < m:
    print('\033[32mEMPRESTIMO APROVADO\033[m')
else:
    print('\033[31mEMPRESTIMO NEGADO\033[m')
#Informaçoes
print('Valor do emprestimo: R$ \033[34m{:.2f}\033[m'.format(n))
print('Quantidade de parcelas \033[33m{}\033[m meses'.format((n2 * 12)))
print('Valor das parcelas: R$ \033[34m{:.2f}\033[m'.format(p))
print('Maximo que voce pode pagar: R$ \033[31m{:.2f}\033[m'.format(m))