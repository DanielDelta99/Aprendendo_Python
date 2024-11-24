c = 's'
total = media = contador = maior = menor = 0
while c in 'sS':
    n = int(input('Digite um número: '))
    total += n
    contador += 1
    if contador == 1:
        maior = menor =n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    c = str(input('Desea continuar [S/N]: '))
media = total/contador
print('''O maior valor digitado foi {}
O menor valor foi {}
A media entre os {} números digitados foi {}.'''.format(maior,menor,contador,media))