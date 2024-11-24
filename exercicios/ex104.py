def leiaint(texto):
    while True:
        numero = input(texto)
        if numero.isnumeric() == True:
            numero = int(numero)
            return numero
            break
        else:
            print('\033[31mERRO! Digite um número inteiro valido\033[m')


n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o valor {n}')
