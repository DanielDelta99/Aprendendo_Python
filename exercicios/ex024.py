# Não funciona direito pois se a palavra for digitada difetente do que apresenta na função in, dara False mesmo sendo  True
n = str(input('Qual o nome da sua cidade? '))
n = n.lower().split() #Divide as palavras e já faz a função do strip/ acrescentei lower depois da correção
n1 = 'santo' in n[0]
print('Sua cidade começa com Santo: {}'.format(n1))

# Solução do professor
n = str(input('Em que cidade você nasceu? ')).strip()
print(n[:5].upper() == 'SANTO')