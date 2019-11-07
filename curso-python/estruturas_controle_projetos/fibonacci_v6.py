# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range(2, quantidade):  # quantidade - 2
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    # listar os 20 primeiros números da sequência
    for fib in fibonacci(20):
        print(fib, end=',')
