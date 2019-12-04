class Data:
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


print(Data(1, 9, 2019))


d1 = Data()
d1.dia = 27
d1.mes = 11
d1.ano = 2019
print(d1)

d2 = Data()
d2.dia = 5
d2.mes = 2
d2.ano = 2021
print(d2)
