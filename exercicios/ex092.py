from datetime import date
dados = {}
dados['Nome'] = str(input('Nome: '))
n = date.today().year
dados['Idade'] = n - int(input('Ano de nascimento: '))
dados['Carteira'] = int(input('N° da carteira de trabalho (0 se não tem): '))
if dados['Carteira'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salário: '))
    dados['Aposentadoria'] = (dados['Contratação'] + 35 - n) + dados['Idade']
print('===== DADOS =====')
for i, j in dados.items():
    print(f'{i} tem o valor {j}')