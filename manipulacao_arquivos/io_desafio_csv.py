from urllib import request
import csv


def read(url):
    with request.urlopen(url) as entrada:
        print('Lendo arquivo .CSV')
        dados_entrada = entrada.read().decode(encoding='latin1')

        for cidades in csv.reader(dados_entrada.splitlines()):
            print(f'{cidades[8]}, {cidades[3]}')


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')


# def download(url):
#     with request.urlopen(url) as entrada,\
#             open('desafio-ibge.csv',  'w') as saida:
#         saida.write(entrada.read().decode(encoding='latin1'))


# download('http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
