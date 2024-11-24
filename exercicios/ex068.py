from random import randint
vitorias = 0
print('---PAR OU IMPAR---')
while True:
    pc = randint(1,10)
    n = int(input('Digite um número de 1 a 10: '))
    op = str(input('Par ou impar [P/I]: ')).upper().strip()
    print('_'*50)
    soma = pc + n
    if 0 > n > 10:
        print('Jogada invalida!!!')
    else:
        if soma % 2 == 0:
            print(f'Você jogou {n} e o computador {pc}. Total deu {soma} PAR')
        else:
            print(f'Você jogou {n} e o computador {pc}. Total deu {soma} IMPAR')
        if soma % 2 == 0 and op == 'P' or soma % 2 == 1 and op == 'I':
            vitorias += 1
            print('Você VENCEU!\nVamos jogar novamente...')
            print('_' * 50)
        else:
            print(f'GAME OVER! Você venceu {vitorias} Vezes.')
            print('_' * 50)
            break


