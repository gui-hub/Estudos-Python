produto = {'nome': 'Caneta Cara', 'preço':
           14.99, 'importada': True, 'estoque': 1347}

for chave in produto.keys():
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)
