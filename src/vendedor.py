from pessoa import Pessoa

class Vendedor(Pessoa):
    def __init__(self, id_vendedor, nome, email):
        super().__init__(nome, email)
        self.id_vendedor = id_vendedor

    def __str__(self):
        return f"Vendedor: {self.id_vendedor} - {self.nome}"
