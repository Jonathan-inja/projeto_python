import json

from insert.inserts import Inserts
from cadastro.cadastro import CadastroGeral

class Common():
    def verificadorUser(nome):
        with open("C:\\Users\\Cicero\\Videos\\projeto-rec\\banco\\clientes.json", encoding='utf-8') as jsonFile:
            user = json.load(jsonFile)

        for indice in range(len(user)):
            if(user[indice]['nome'] == nome):
                return True

class Baixa():
    def autenticator():
        user = input("Digite o nome do Cliente:")
        if(Common.verificadorUser(user)):
            with open("C:\\Users\\Cicero\\Videos\\projeto-rec\\banco\\produtos.json", encoding='utf-8') as jsonFile:
                Baixa.baixa(user,jsonFile)

        else:
            print("Usuario ainda não cadastrado!")
            
            while True:
                print("=== Desejá cadastrar cliente ou realizar a baixa do produto? ===")
                print('''
                [1] - cadastrar cliente
                [2] - Continuar e dar baixa no produto
                [3] - Encerrar!
                ''')
                escolha = int(input(":"))
                if(escolha == 1):
                    CadastroGeral.cadastroCliente()
                elif(escolha == 2):
                    with open("C:\\Users\\Cicero\\Videos\\projeto-rec\\banco\\produtos.json", encoding='utf-8') as jsonFile:
                        Baixa.baixa("", jsonFile)
                elif(escolha == 3):
                    break
                else:
                    print("Opção não encontrada por favor digitá novamente o numero da opção!!!")

    def baixa( user,jsonFile):
        escolha = json.load(jsonFile)
        print("==================== Itens Disponiveis =====================")
        for indice in range(len(escolha)):
            print(f"[{indice}]      {escolha[indice]['nome_do_produto']} ---------------------- R$ {escolha[indice]['preco']}")
            

        pedidoCliente = int(input(":"))
        valorPago = float(input("Digita valor pago:"))
        troco = valorPago - float(escolha[pedidoCliente]['preco'])
        print(f"Troco Do Cliente:{troco}")
        Inserts.nota(user,pedidoCliente,valorPago,troco)