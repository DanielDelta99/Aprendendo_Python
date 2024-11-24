# Com a correçao do pr eliminei dois ifs. if n == 0 e if numero < min(lista). reduçao de 6 linhas
lista = []
for n in range(0,5):
    numero = int(input('Digite um número: '))
    if n == 0 or numero > max(lista):
        lista.append(numero)
        print('Adicionado ao fim da fila')
    else:
        for i,m in enumerate(lista):
            if numero < m:
                lista.insert(i,numero)
                print(f'Adicionado na posição {i}')
                break
print(lista)
