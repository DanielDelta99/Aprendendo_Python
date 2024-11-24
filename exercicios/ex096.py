def area(a,b):
    c = a * b
    print(f'''A area do terreno é {c:.1f} m2.
pois {a} X {b} = {c:.1f}''')


a = int(input('Largura (m): '))
b = int(input('Altura (m): '))
area(a,b)