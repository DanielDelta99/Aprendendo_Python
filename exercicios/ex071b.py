n = int(input())
cedula = (200,100,50,20,10,5,2,1)
for i in (cedula):
    if n//i:
        m = n//i
        c = 'moedas' if n == 1 else 'cedulas'
        n -= m*i
        print(f'Total de {m} {c} de R$ {i:.2f}')
