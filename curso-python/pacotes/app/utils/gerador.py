from random import choice


def novo_nome():
    return choice([
        'Guilherme',
        'Erasmo',
        'Zilda',
        'Paloma',
        'Jose',
        'Gabriel',
        'Eva',
    ])


print(f'{__name__} , {__package__} = {novo_nome.__name__}')
