
#Entrada de dados
print('para qual base deseja converter')
print('[1] Binario \n[2] Octa \n[3] Hexadecimal')
n = int(input())
n2 = int(input('Digite um numero para a conversão: '))
if n == 1:
    print(bin(n2)[2:])
elif n == 2:
    print(oct(n2)[2:])
elif n == 3:
    print(hex(n2)[2:])
else:
    print('Opção invalida!!!')