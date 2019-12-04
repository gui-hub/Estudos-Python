from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.data = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluída)' if self.feito else '')


def main():
    casa = []
    casa.append(Tarefa('Ir no banheiro'))
    casa.append(Tarefa('Voltar do banheiro'))

    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Voltar do banheiro' or tarefa.descricao == 'Ir no banheiro']
    for tarefa in casa:
        print(f'- {tarefa}')


main()
