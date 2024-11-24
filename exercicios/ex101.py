from datetime import date

def voto(a):
    anoatual = date.today().year
    idade = anoatual - a
    print(f'Com {idade} anos: ',end='')
    if idade < 18:
        return(f'NAO VOTA')
    elif idade > 65:
        return('VOTO OPCIONAL')
    else:
        return('VOTO OBRIGATORIO')
ano_nasc = int(input('Ano que você nasceu: '))
retorno = voto(ano_nasc)
print(retorno)