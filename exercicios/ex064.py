contador = 0
soma = 0
n = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        contador += 1
        soma += n
print('Você digitou {} termos e a soma entre eles é {}'.format(contador,soma))