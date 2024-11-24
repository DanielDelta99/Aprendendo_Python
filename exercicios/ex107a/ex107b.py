from ex107a import moeda

num = float(input('Digite o preço: '))
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'O dobro de {num} é {moeda.dobro(num)}')
p = int(input('Digite uma porcentagem: '))
print(f'''Aumentando {p}%, temos {moeda.almentando(num,p)}
Diminuindo {p}%, temos {moeda.diminuindo(num,p)}''')