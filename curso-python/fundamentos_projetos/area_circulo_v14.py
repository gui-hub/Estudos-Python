from math import pi
import sys
import errno


def help():
    print("É necessário informar o raio do círculo.")
    print(f"Sintaxe: {sys.argv[0][-19:]} <raio>")


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print('O raio deve ser um valor número')
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do círculo', area)
