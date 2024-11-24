n = int(input())
if n//200:
    n200 = n//200
    n -= n200*200
    print(f'Total de {n200} celulas de R$ 200,00')
if n//100:
    n100 = n//100
    n -= n100*100
    print(f'Total de {n100} celulas de R$ 100,00')
if n//50:
    n50 = n//50
    n -= n50*50
    print(f'Total de {n50} celulas de R$ 50,00')
if n//20:
    n20 = n//20
    n -= n20*20
    print(f'Total de {n20} celulas de R$ 20,00')
if n//10:
    n10 = n//10
    n -= n10*10
    print(f'Total de {n10} celulas de R$ 10,00')
if n//5:
    n5 = n//5
    n -= n5*5
    print(f'Total de {n5} celulas de R$ 5,00')
if n//2:
    n2 = n//2
    n -= n2*2
    print(f'Total de {n2} celulas de R$ 2,00')
if n//1:
    n1 = n//1
    n -= n1*1
    print(f'Total de {n1} moedas de R$ 1,00')
