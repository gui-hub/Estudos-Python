def get_tipo_dia(dia):
    dias = {
        (1, 7): 'Fim de semana',
        tuple(range(2, 8)): 'Dia de Semana'
    }
    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros)
    return next(dia_escolhido, '** inválido **')


if __name__ == '__main__':
    for dia in range(9):
        print(f'{dia}, {get_tipo_dia(dia)}')
