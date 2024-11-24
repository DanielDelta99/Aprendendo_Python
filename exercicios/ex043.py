p = float(input('Digite seu peso Kg: '))
if p == 999:
    imc = float(input())
else:
    a = float(input('Digite sua altura m: '))
    imc = p/a**2
    print('Seu imc é {:.1f} e você está'.format(imc),end=' ')
if imc < 18.5:
    print('abaixo do peso')
elif imc < 25:
    print('com o peso ideal')
elif imc < 30:
    print('com sobrepeso')
elif imc < 40:
    print('obeso')
else:
    print('com obesidade mórbida')
