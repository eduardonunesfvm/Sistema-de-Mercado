from datetime import datetime

class Venda:
    def __init__(self, id_venda, cliente, vendedor, produtos):
        self.id_venda = id_venda
        self.cliente = cliente
        self.vendedor = vendedor
        self.produtos = produtos
        self.data = datetime.now().strftime("%d/%m/%Y")

    def total(self):
        return sum(produto.preco for produto in self.produtos)

    def __str__(self):
        return f"Venda {self.id_venda} - Cliente: {self.cliente.nome} - Total: R${self.total():.2f}"