from random import randint


def sortear_dado():
    return randint(1, 6)


var = sortear_dado()

for i in range(1, 7):
    if i % 2 == 1:
        continue

    if var == i:
        print('ACERTOU', i, var)
        break
else:
    print('Não acertou o número!')
