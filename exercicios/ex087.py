matrix = [[0,0,0],[0,0,0],[0,0,0]]
soma = coluna = 0
for i in range(0,3):
    for j in range(0,3):
        matrix[i][j] = int(input(f'Digite um valor para [{i,j}]: '))
print('=+='*11)
for i in range(0,3):
    coluna += matrix[i][2]
    for j in range(0,3):
        if matrix[i][j] % 2 == 0:
            soma += matrix[i][j]
        print(f'[{matrix[i][j]}]',end='')
    print()
print('=+='*11)
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da 3° coluna é {coluna}')
print(f'O maior valor da 2° linha é {max(matrix[1][:])}')
