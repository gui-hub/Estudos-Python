def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    todos_params('a', 'b', 'c')
    todos_params(1, 2, 3, primeiro=1, segundo=2, terceiro=4)
    todos_params('guilherme', 23, False, guilherme=24, idade=True)
