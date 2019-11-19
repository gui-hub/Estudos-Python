def tag_bloco(conteudo, classe='sucesso', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('TEXTO VAI AQUI', classe='text', inline=True))
    print(tag_bloco('TEXTO VAI AQUI'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
