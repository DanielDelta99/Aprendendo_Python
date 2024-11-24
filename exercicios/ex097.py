def escreva(msg):
    n = len(msg)+4
    print('='*n)
    print(f'  {msg}  ')
    print('='*n)


escreva(str(input('Escreva uma mensagem: ')))
