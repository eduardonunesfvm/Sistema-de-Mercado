from produto import Produto
from cliente import Cliente
from vendedor import Vendedor
from venda import Venda

def carregar_dados():
    try:
        with open("dados/produtos.txt", "r") as arquivo:
            for linha in arquivo:
                id_produto, nome, preco = linha.strip().split(";")
                produtos.append(Produto(id_produto, nome, float(preco)))
    except:
        pass

    #clientes
    try:
        with open("dados/clientes.txt", "r") as arquivo:
            for linha in arquivo:
                id_cliente, nome, email = linha.strip().split(";")
                clientes.append(Cliente(id_cliente, nome,))
    except:
        pass

    try:
        with open("dados/vendedores.txt", "r") as arquivo:
            for linha in arquivo:
                id_vendedor, nome, email = linha.strip().split(";")
                vendedores.append(Vendedor(id_vendedor, nome, email))
    except:
        pass


produtos = []
vendas = []
clientes = []
vendedores = []

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastrar Produto")
        print("2 - Cadastrar Cliente")
        print("3 - Cadastrar Vendedor")
        print("4 - Listar Produtos")
        print("5 - Registrar Venda")
        print("6 - Listar Vendas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            cadastrar_cliente()
        elif opcao == "3":
            cadastrar_vendedor()
        elif opcao == "4":
            listar_produtos()
        elif opcao == "5":
            registrar_venda()
        elif opcao == "6":
            listar_vendas()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

def cadastrar_produto():
    try:  
        id_produto = input("Digite o ID do produto")
        nome = input("Nome: ")
        preco = float(input("Preço:"))
        produto = Produto(id_produto, nome, preco)
        produtos.append(produto)

        with open("dados/produtos.txt", "a") as arquivo:
            arquivo.write(f"{id_produto};{nome};{preco}\n")

        print("Produto cadastrado e salvo!")
    except:
        print("Erro ao cadastrar produto!")


def cadastrar_cliente():
    id_cliente = input("ID do cliente: ")
    nome = input("Nome: ")
    email = input("Email: ")
    cliente = Cliente(id_cliente, nome, email)
    clientes.append(cliente)

    with open("dados/clientes.txt", "a") as arquivo:
        arquivo.write(f"{id_cliente};{nome};{email}")
   

def cadastrar_vendedor():
    id_vendedor = input("ID do vendedor: ")
    nome = input("Nome: ")
    email = input("Email: ")
    vendedor = Vendedor(id_vendedor, nome, email)
    vendedores.append(vendedor)

    with open("dados/vendedores.txt", "a") as arquivo:
        arquivo.write(f"{id_vendedor};{nome};{email}")


def listar_produtos():
    print("\nLISTA DE PRODUTOS:")
    for p in produtos:
        print(p)

def registrar_venda():
    if not clientes or not vendedores or not produtos:
        print("Cadastre clientes, vendedor e produto antes de vender.") 
        return
    id_venda = input("ID da venda: ")

    print("\nClientes disponíveis:")
    for c in clientes:
        print(c)
    cliente_id = input("Informe o ID do cliente: ")
    cliente = next((c for c in clientes if c.id_cliente == cliente_id), None)

    print("\nVendedores disponíveis:")
    for v in vendedores:
        print(v)
    vendedor_id = input("Informe o ID do vendedor: ")
    vendedor = next((v for v in vendedores if v.id_vendedor == vendedor_id), None)

    produtos_venda = []
    while True:
        listar_produtos()
        prod_id = input("Digite o ID do produto (0 para finalizar): ")
        if prod_id == "0":
            break
        produto = next((p for p in produtos if p.id_produto == prod_id), None)
        if produto:
            produtos_venda.append(produto)
        else:
            print("Produto não encontrado!")

    if produtos_venda:
        venda = Venda(id_venda, cliente, vendedor, produtos_venda)
        vendas.append(venda)
        print("\nVenda registrada com sucesso!")
    else:
        print("Nenhum produto selecionado!")


def listar_vendas():
    print("\nHISTÓRICO DE VENDAS:")
    for v in vendas:
        print(v)


carregar_dados()
menu()
