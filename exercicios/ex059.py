opcao = 0
r = 0
numeros = True
while opcao != 5:
    if numeros == True:
        n1 = int(input('1° Número: '))
        n2 = int(input('2° Número: '))
    numeros = False
    opcao = int(input('''--------------- MENU ---------------
[1] Somar
[2] Multiplicar
[3] Qual o maior
[4] Novos números
[5] Sair do programa
>>>Qual é a sua opção? '''))
    print('-'*36)
    if opcao == 1:
        r = n1 + n2
        print('A soma entre {} + {} = {}'.format(n1,n2,r))
    elif opcao == 2:
        r = n1 * n2
        print('A multiplicação entre {} X {} = {}'.format(n1,n2,r))
    elif opcao == 3:
        if n1 > n2:
            r = n1
        else:
            r = n2
        print('O mais numero entre {} e {} é {}'.format(n1,n2,r))
    elif opcao == 4:
        print('Digite os números novamente')
        numeros = True
    elif opcao == 5:
        print('Obrigado por usar nosso programa!!!')
    else:
        print('Opção invalida')
