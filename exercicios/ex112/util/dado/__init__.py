def leiadin(msg):

    while True:
        numero = True
        nu = input(msg).strip()

        num = nu.replace(',', '.')
        if num.count('.') >= 2:
            numero = False
        if num.count('.') == 1 and len(num) == 1:
            numero = False
        num = num.replace('.','0')
        if num.isnumeric() == False:
            numero = False

        if numero == False:
            print(f'\033[31mERRO: "{nu}" é um preço inválido!\033[m')
        else:
            nu = num.replace(',','.').strip()
            return float(num)
            break

