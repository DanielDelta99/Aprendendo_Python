def linha(tipo='-',tamanho=47):
    return f'{tipo}' * tamanho

def cabeçalho(msg,tamanho=47):
    print(linha(tamanho=tamanho))
    print(f'{msg.center(tamanho)}')
    print(linha(tamanho=tamanho))