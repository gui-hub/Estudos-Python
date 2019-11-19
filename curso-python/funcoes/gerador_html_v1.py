#! python
def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    # Testes (assertions)
    assert tag_bloco('Incluído com sucesso!') == \
        '<div class="success">Incluído com sucesso!</div>'

    assert tag_bloco('Impossivel de excluir!', 'error') == \
        '<div class="error">Impossivel de excluir!</div>'

    print(tag_bloco('bloco'))

    # class TestTag:
    #     def test_tag_ok(self):
    #         assert tag_bloco('Incluido com sucesso!') == \
    #             '<div class="success">Incluido com sucesso!</div>'

    #     def test_tag_error(self):
    #         assert tag_bloco('Impossivel excluir!', 'error') == \
    #             '<div class="error">Impossivel excluir!</div>'
