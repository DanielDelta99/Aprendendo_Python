frase = '     Curso em Vídeo Python    '
print(frase.strip()[::])
print(frase.upper().count('O'))
print(len(frase.strip()))
frase = (frase.replace('Curso','Jabasinho'))
print(frase.strip())
frase = (frase.replace('Python','Fubá'))
frase = frase.split()
print(frase)
n = len(frase)
print(type(n),n)
print('A Primeira palavra é = {} \nE a segunda palavra é = {}'.format(frase[0],frase [n - 1]))
# Consegui