class Produto:
    def __init__(self, id_produto, nome, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.id_produto} - {self.nome} - R${self.preco:.2f}"