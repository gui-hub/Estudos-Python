import csv
from urllib import request
from time import sleep


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o CSV...')
        dados = entrada.read().decode(encoding='latin1')
        print('Download Completo!')
        sleep(0.5)
        print('Aguarde 2 segundos para exibição...')
        sleep(2)

        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    read('http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
