# Resultado pos correção/ logica correta, mas com linhas desnecessarias
x = int(input('1° Número: '))
y = int(input('2° Número: '))
z = int(input('3° Número: '))
if x > y and x > z:
    n = x
if y > x and y > z:
    n = y
else:
    n = z
if x < y and x < z:
    n1 = x
if y < x and y < z:
    n1 = y
else:
    n1 = z
print('O maior número é {}, e o menor é {}'.format(n,n1))