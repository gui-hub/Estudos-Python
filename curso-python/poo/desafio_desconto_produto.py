class Produto:
    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco

    def desconto(self, desconto=0.05):
        valor_inicial = self.preco
        valor_desconto = valor_inicial * desconto
        self.preco -= valor_desconto if desconto else 0
        return self.preco

    def __str__(self):
        return f'Produto: {self.produto} \nPreço com desconto: R$ {self.preco:.3f}'


if __name__ == '__main__':
    p1 = Produto('Televisão LED 32', 3.200)
    desconto = p1.desconto(desconto=0.15)
    print(p1)
