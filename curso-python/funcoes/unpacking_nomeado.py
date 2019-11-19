def resultado_f1(primeiro, segundo, terceiro):
    print(f'Posicao 1 --> {primeiro}')
    print(f'Posicao 2 --> {segundo}')
    print(f'Posicao 3 --> {terceiro}')


if __name__ == '__main__':
    podium = {'segundo': 'Piloto2',
              'primeiro': 'Piloto1',
              'terceiro': 'Piloto3'}
    resultado_f1(**podium)
