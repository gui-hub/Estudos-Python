import csv

with open('pessoas.csv', encoding='latin1') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade:{}' .format(*pessoa))
