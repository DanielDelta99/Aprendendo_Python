from ex108 import moeda

num = float(input('Digite o preço: '))
print(f'A metade de {moeda.fmoeda(num)} é {moeda.fmoeda(moeda.metade(num))}')
print(f'O dobro de {moeda.fmoeda(num)} é {moeda.fmoeda(moeda.dobro(num))}')
p = int(input('Digite uma porcentagem: '))
print(f'''Aumentando {p}%, temos {moeda.fmoeda(moeda.almentando(num,p))}
Diminuindo {p}%, temos {moeda.fmoeda(moeda.diminuindo(num,p))}''')