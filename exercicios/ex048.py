t = 0
c = 0
for n in range(1,501,2):
    if n % 3 == 0:
        t += n
        c += 1
print('{} Números com uma soma de {}'.format(c,t))