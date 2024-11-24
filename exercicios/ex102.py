def fatoriall(num,show=False):
    """
    -> Calcule o fatorial de qualquer número:
    :param num: Número a ser fatorado. Obrigatorio
    :param show: Mortrar ou não a conta. Opcional
    :return: Retorna o resultado do valor de num.
    """
    mult = 1
    while num != 0:
        if show == True:
            print(f'{num}',end='')
            if num != 1:
                print(f' X ', end='')
            else:
                print(' = ',end='')
        mult *= num
        num -= 1
    return mult


print(fatoriall(5,True))
help(fatoriall)