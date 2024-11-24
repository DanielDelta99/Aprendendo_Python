tupla = ('Lápis',1.75,'Borracha',2,'Caderno',15.9,'Estojo',25,'Transferidor',4.2
         ,'Compasso',9.99,'Mochila',120.32,'Canetas',22.3,'Livro',34.9)
print('='*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('='*40)
for c1 in range(0,len(tupla),2):
    c2 = c1 + 1
    print(f'{tupla[c1]:.<30} R$ {tupla[c2]:.2f}')
print('='*40)