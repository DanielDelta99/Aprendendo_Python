print('TEXTE DE CARACTERISTICAS DE CARACTERES')
n = input('Digite alguma coisa: ')
print(type(n))
print('Alfanumerico: ',n.isalnum())
print('Alfabetico: ',n.isalpha())
print('Dentro da normativa ASCII:',n.isascii())
print('São todos digitos:',n.isdigit())
print('Tudo minusculo: ',n.islower())
print('É um espaço em branco: ',n.isspace())
print('Decimal: ',n.isdecimal())
print('Pode ser uma variavel:',n.isidentifier())
print('Todos caracteres são numericos; ',n.isnumeric())
print('Imprimíveis: ',n.isprintable())
print('Primeira maiuscula: ',n.istitle())
print('Todos em maiusculo: ',n.isupper())
