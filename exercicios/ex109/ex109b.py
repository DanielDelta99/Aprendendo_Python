from ex109 import moeda

num = float(input('Digite o preço: '))
print(f'A metade de {moeda.fmoedas(num)} é {moeda.metade(num,True)}')
print(f'O dobro de {moeda.fmoedas(num)} é {moeda.dobro(num,True)}')
p = int(input('Digite uma porcentagem: '))
print(f'''Aumentando {p}%, temos {moeda.almentando(num,p,True)}
Diminuindo {p}%, temos {moeda.diminuindo(num,p,True)}''')