def fibonacci(sequencia=None):
    # sequencia = sequencia or [0,1]
    sequencia = [0, 1] if sequencia == None else sequencia
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))
    assert restart == [0, 1, 1]
