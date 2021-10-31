class Turma:
    def __init__(self, id=0, ano=0, curso="", alunos=[]):
        self.id = id
        self.ano = ano
        self.curso = curso
        self.alunos = alunos

    def to_dict(self):
        turma = {}
        for attr, value in self.__dict__.items():
            turma[attr] = value

        turma['alunos'] = [aluno.to_dict() for aluno in self.alunos]

        return turma

class Aluno:
    def __init__(self, id=0, nome="", matriculado=True):
        self.id = id
        self.nome = nome
        self.matriculado = matriculado

    def to_dict(self):
        aluno = {}
        for attr, value in self.__dict__.items():
            aluno[attr] = value
        return aluno