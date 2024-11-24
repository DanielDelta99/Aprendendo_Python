maior = homens = mulheres = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Genero[M/F]: ')).upper().strip()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    elif idade < 20:
        mulheres += 1
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Continuar[S/N]: ')).upper().strip()[0]
    if stop == 'N':
        print('Programa finalizado!!!')
        break
print(f'''Pessoas com mais de 18 anos: {maior}
Homens cadastrados: {homens}
Mulheres com  menos de 20 anos: {mulheres}''')