lista = []
lista.append(input('Digite uma expressão: '))
if lista[0].count('(') == lista[0].count(')'):
    print('Essa é uma expressão valida')
else:
    print('Essa é uma expressão invalida')