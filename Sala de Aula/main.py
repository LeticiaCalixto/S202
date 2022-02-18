from aluno import Aluno
from aula import Aula
from professor import Professor


aluno1 = Aluno(
    nome = "Leticia",
    matricula = "1582",
    curso = "GEC",
    periodo = 7
)

aluno2 = Aluno(
    nome = "Cecilia",
    matricula = "1610",
    curso = "GEC",
    periodo = 7
)

aluno3 = Aluno(
    nome = "Carlos",
    matricula = "1554",
    curso = "GEC",
    periodo = 7
)

aluno4 = Aluno(
    nome = "Marina",
    matricula = "1553",
    curso = "GEC",
    periodo = 7
)

alunos = [aluno1, aluno2, aluno3, aluno4]

professor = Professor(nome = "Renzo", especialidade = "Banco de Dados")

aula = Aula(assunto = "MongoDB", professor = professor, alunos = alunos )

print(aula.getListaPresenca())