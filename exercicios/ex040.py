n1 = float(input('1° Nota: '))
n2 = float(input('2° Nota: '))
m = (n1+n2)/2
if m >= 7:
    print('Sua media: {:.1f}\n\033[34mAPROVADO\033[m'.format(m))
elif m >= 5 and m <= 6.9:
    print('Sua media: {:.1f}\n\033[33mRECUPERAÇÃO\033[m'.format(m))
else:
    print('Sua media: {:.1f}\n\033[31mREPROVADO\033[m'.format(m))
