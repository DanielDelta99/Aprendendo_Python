# Forma do professor
def notas(*nota,sit=False):
    """
    => ex105
    :param nota: Recebe varios valores de notas
    :param sit: situcao é opcional
    :return: retorna um dicionario com varias depuraçoes
    """
    dicio = {}
    dicio['Total'] = len(nota)
    dicio['Maior'] = max(nota)
    dicio['Menor'] = min(nota)
    dicio['Media'] = sum(nota)/len(nota)
    if sit:
        if dicio['Media'] > 7:
            dicio['situação'] = 'Boa'
        elif dicio['Media'] < 6:
            dicio['situação'] = 'Ruim'
        else:
            dicio['situação'] = 'Rasoavel'
    return dicio


resp = notas(5,6,6,6,0,sit = True)
print(resp)
