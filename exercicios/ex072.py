numeros = ('zero','um','dois','três','Quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    n = int(input('Digite um número de 1 a 20: '))
    if -1 < n < 21:
        break
print(f'Você digitou {numeros[n]}')