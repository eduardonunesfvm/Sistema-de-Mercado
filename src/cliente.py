from carrinho import Carrinho
from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, id_cliente, nome, email):
        super().__init__(nome, email)
        self.id_cliente = id_cliente
        self.carrinho = Carrinho()

    def __str__(self):
        return f"{self.id_cliente} - {self.nome} - {self.email}"