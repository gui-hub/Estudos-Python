MAIOR_IDADE = 18


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        if not self.idade:  # if self.idade nao estiver setado
            self.idade
        else:
            return f'{self.nome}, {self.idade} anos'

    def isAdult(self):
        return self.idade >= MAIOR_IDADE  # return self.idade IF SELF.IDADE > MAIOR_IDADE ("se for maior que")
