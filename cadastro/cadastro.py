from insert.inserts import Inserts
# dados = Inserts()
class CadastroGeral():
    def cadastroCliente():
        nome=input("Nome completo: ")
        cpf=input("CPF: ")
        idade=input("Idade: ")
        telefone=input("Telefone: ")
        senha=input("Senha: ")

        Inserts.insertClient(nome,cpf,idade,telefone,senha)
    
    def cadastroDoProduto():
        nome=input("Nome do produto: ")
        preco=input("Preço do produto: ")
        Inserts.insertProdutos(nome, preco)