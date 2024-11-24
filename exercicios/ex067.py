while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('_'*35)
    if n < 0:
        print('PROGRAMA FINALIZADO.')
        break
    for c in range(1,11):
        print(f'{n} X {c:2} = {n*c}')
    print('_'*35)