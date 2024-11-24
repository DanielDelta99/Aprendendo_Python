from poo.banco.interface import linha, cabecalho


class Pessoa:
    def __init__(self,nome,idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self,idade):
        self._idade = idade


class Aluno(Pessoa):
    def __init__(self,nome,idade,matricula):
        super().__init__(nome,idade)
        self._matricula = matricula
        self._diciplinas = []

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self,numero):
        self._matricula = numero

    @property
    def diciplinas(self):
        return self._diciplinas

    @diciplinas.setter
    def diciplinas(self,nome):
        self._diciplinas = nome

    def add_disciplinas(self,nome):
        self._diciplinas.append(nome)

class Professor(Pessoa):
    def __init__(self,nome,idade,salario,):
        super().__init__(nome,idade)
        self._salario = salario
        self._diciplinas = []

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        self._salario = valor

    @property
    def diciplinas(self):
        return self._diciplinas

    @diciplinas.setter
    def diciplinas(self,nome):
        self._diciplinas = nome

    def add_disciplinas(self,nome):
        self._diciplinas.append(nome)


class Diciplina:
    def __init__(self,nome,professor):
        self._nome = nome
        self._professor = professor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def professor(self):
        return self._professor

    @professor.setter
    def professor(self, professor):
        self._professor = professor


class Turma:
    def __init__(self, nome_turma, diciplina):
        self._nome_turma = nome_turma
        self._diciplina = diciplina
        self._alunos = []

    @property
    def nome_turma(self):
        return self._nome_turma

    @nome_turma.setter
    def nome_turma(self, nome):
        self._nome_turma = nome

    @property
    def diciplina(self):
        return self._diciplina

    @diciplina.setter
    def diciplina(self, diciplina):
        self._diciplina = diciplina

    @property
    def alunos(self):
        return self._alunos

    @alunos.setter
    def alunos(self, nome):
        self._alunos = nome

    def add_alunos(self,nome):
        self._alunos.append(nome)


    def exibir_turma(self):
        cabecalho('Classe')
        print(f'Nome da turma: {self.nome_turma}')
        print(f'Disciplina: {self.diciplina.nome}')
        print(f'Professor: {self.diciplina.professor.nome}')
        print(f'Alunos:')
        linha()
        for aluno in self.alunos:
            print(aluno.nome)