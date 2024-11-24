n = int(input('Qual a velocidade do seu carro Km/h: '))
if n > 80:
    print('VOCE FOI MULTADO!!!')
    n1 = (n - 80) * 7
    print('Você esta a {}Km/h acima da velocidade permitida. Sua multa ficou no valor de R${:.2f}'.format(n-80,n1))
else:
    print('VOCE ESTA DENTRO DA VELOCIDADE PERMITIDA')