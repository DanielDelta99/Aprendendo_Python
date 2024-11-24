numero = (int(input('Digite 1° número: ')),int(input('Digite 2° número: ')),int(input('Digite 3° número: ')),int(input('Digite 4° número: ')))
print(f'Você digitou os numeros {numero}')
print(f'O número 9 aparece {numero.count(9)} vezes.')
if numero.count(3) > 0: # if 3 in numero:
    print(f'O valor 3 aprece na {numero.index(3)+1}° posição')
else:
    print(f'O valor 3 não foi digitado')
par = 0
print(f'Os valores pares digitados foram ',end='')
for n in numero:
    if n % 2 == 0:
        print(n,end=' ')

