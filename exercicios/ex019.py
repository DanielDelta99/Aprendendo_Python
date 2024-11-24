# Não precisava mostrar o numero.
import random
n1 = str(input('Nome aluno 01: '))
n2 = str(input('Nome aluno 02: '))
n3 = str(input('Nome aluno 03: '))
n4 = str(input('Nome aluno 04: '))
alunos = {1: n1, 2: n2, 3: n3, 4: n4}
na = random.choice(list(alunos.keys()))
nn = alunos[na]
print('O aluno {}, {}, deve apagar o quadro'.format(na,nn))
