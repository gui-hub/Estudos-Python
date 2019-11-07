# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(n):
    if n <= 1:
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))


var = 20

if __name__ == '__main__':
    for fib in range(var):
        print(fibonacci(fib))
