from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

    def toString(self):
        return f'''
        Nome: {self.nome}
        Especialidade: {self.especialidade}
        '''