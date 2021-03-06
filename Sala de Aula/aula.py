class Aula():
    def __init__(self, professor, alunos, assunto):
        self.professor = professor
        self.alunos = alunos
        self.assunto = assunto

    def getListaPresenca(self):
        result = f"Aula de {self.assunto} \n \n Professor: {self.professor.nome} \n \n Alunos Presentes:"

        for aluno in self.alunos:
            result += aluno.toString()

        return result