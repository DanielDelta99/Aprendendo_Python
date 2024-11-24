from poo.escola.Escola import *

daniel = Aluno('Daniel',26,99)
amanda = Aluno('Amanda',23,100)

jose = Professor('Jose',33,1800)
jose.add_disciplinas('Fisica')
jose.add_disciplinas('Matematica')

matematica = Diciplina('matematica',jose)

t1 = Turma('T1',matematica)
t1.add_alunos(daniel)
t1.add_alunos(amanda)

t1.exibir_turma()