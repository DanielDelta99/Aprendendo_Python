total = p1000 = barato = 0
print('-'*40)
print('{:^40}'.format('LOJAS LOJAS'))
print('-'*40)
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    total += preco
    if preco >= 1000:
        p1000 += 1
    if preco < barato or barato == 0:
        barato = preco
        nomeb = nome
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if stop == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'''O total da compra foi de R$ {total:.2f}
Temos {p1000} produtos custando mais de R$ 1000,00
O produto mais barato foi {nomeb} e custou R$ {barato:.2f}''')