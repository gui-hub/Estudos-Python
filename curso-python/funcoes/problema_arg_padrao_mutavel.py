def fibonacci(sequencia=(0, 1)):
    return sequencia + (sequencia[-1] + sequencia[-2],)


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    inicio = fibonacci(inicio)
    print(inicio, id(inicio))
    restart = fibonacci()
    print(restart, id(restart))
