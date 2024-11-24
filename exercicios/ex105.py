def notas(*nota,sit=False):
    """
    => ex105
    :param nota: Recebe varios valores de notas
    :param sit: situcao é opcional
    :return: retorna um dicionario com varias depuraçoes
    """
    total = maior = menor = media = 0
    dicio = {}
    for n in nota:
        total += 1
        if total == 1:
            maior = menor = n
        elif n > maior:
            maior = n
        elif n < menor:
            menor = n
        media += n
    media = media/total
    dicio = {'total':total,'maior':maior,'menor':menor,'media':media}
    if sit == True:
        if media > 7:
            dicio['situação'] = 'Boa'
        elif media < 6:
            dicio['situação'] = 'Ruim'
        else:
            dicio['situação'] = 'Rasoavel'
    return dicio

resp = notas(5,6,6,6,0,sit = True)
print(resp)
help(notas)