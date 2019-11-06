def get_dia_final_semana(dia):
    dias = {
        0: 'Domingo',
        1: 'Sábado',
    }
    return dias.get(dia, '** inválido **')


def get_dia_util_semana(dia):
    dias = {
        0: 'Segunda',
        1: 'Terça',
        2: 'Quarta',
        3: 'Quinta',
        4: 'Sexta',
    }
    return dias.get(dia, '** inválido **')


if __name__ == '__main__':
    while True:
        user = int(input('Digite o dia da semana: '))
        if user == -1:
            print('SAINDO!')
            break
        elif user == 1:
            print(get_dia_util_semana(0))
        elif user == 2:
            print(get_dia_util_semana(1))
        elif user == 3:
            print(get_dia_util_semana(2))
        elif user == 4:
            print(get_dia_util_semana(3))
        elif user == 5:
            print(get_dia_util_semana(4))
        elif user == 6:
            print(get_dia_final_semana(0))
        elif user == 7:
            print(get_dia_final_semana(1))
        else:
            print('Digite um número entre 1 e 7, -1 PARAR')
