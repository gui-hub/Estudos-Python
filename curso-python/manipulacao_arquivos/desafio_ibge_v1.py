import csv

with open('desafio-ibge.csv') as arquivo:
    for cidades in csv.reader(arquivo):
        print(f'{cidades[3]}, {cidades[8]}')
