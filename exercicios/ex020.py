from random import shuffle
n1 = str(input('Nome aluno 01: '))
n2 = str(input('Nome aluno 02: '))
n3 = str(input('Nome aluno 03: '))
n4 = str(input('Nome aluno 04: '))
alunos = [n1,n2,n3,n4]
shuffle(alunos)
print(alunos)

