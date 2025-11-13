class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto):
        self.itens.append(produto)

    def retirar_item(self, produto):
        if produto in self.itens:
            self.itens.remove(produto)
            print(f"{produto.nome} removido do carrinho.")
        else:
            print("Esse item não está no carrinho!")
        

    def total(self):
        return sum(produto.preco for produto in self.itens)

    def listar_itens(self):
        for item in self.itens:
            print(item)