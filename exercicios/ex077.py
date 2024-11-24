tupla = ('Daniel ','Amanda ','Chaninha ','Raquel ','Nael ','Cosme ',
          'Eliete ','Jessica ','Joao ','Lu ','Paulo ','Pedro ')
print(f'{"Nomes ":=<30} {"Vogais"}')
for c in tupla:
    print(f'{c:.<30}',end = ' ')
    for c1 in range(0,len(c)):
        if c[c1].lower() in 'aeiou':
            print(c[c1],end = ' ')
    print()
