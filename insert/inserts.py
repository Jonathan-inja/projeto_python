import json
from os import path
import datetime
class Inserts():
    def insertClient(nome,cpf,idade,telefone,senha):

 
        filename = "C:\\Users\\Cicero\\Videos\\projeto-rec\\banco\\clientes.json"
        listObj = []
        
        
        # Lendo o arquivo json
        with open(filename) as fp:
            listObj = json.load(fp)
            listObj.append({
            "nome":nome,
            "cpf": cpf,
            "idade": idade,
            "telefone": telefone,
            "senha":senha

            })
        
        with open(filename, 'w') as json_file:
            json.dump(listObj, json_file, 
                                indent=4,  
                                separators=(',',': '))
        
        print('Usuario cadastrado Com sucesso')
    
    def insertProdutos(nomeDoProduto,preco):
        filename = "C:\\Users\\Cicero\\Videos\\projeto-rec\\banco\\produtos.json"
        listObj = []
        with open(filename,  encoding='utf-8') as fp:
            listObj = json.load(fp)
            listObj.append({
            "nome_do_produto":nomeDoProduto,
            "preco": preco,
            })
        
        with open(filename, 'w') as json_file:
            json.dump(listObj, json_file, 
                                indent=4,  
                                separators=(',',': '))
        
        print('Pedido Inserido no Menu!')

    def nota(nomeCliente,pedidoCliente,valorPago,troco):
        with open("C:\\Users\\Cicero\\Videos\\projeto-rec\\banco\\notaFiscal.json", encoding='utf-8') as fp:
            listObj = json.load(fp)
            listObj.append({
                "nome_do_cliente":nomeCliente,
                "pedido_do_cliente": pedidoCliente,
                "valor_pago": valorPago,
                "troco": troco,
                "data": str(datetime.datetime.now())
            })
        
        with open("C:\\Users\\Cicero\\Videos\\projeto-rec\\banco\\notaFiscal.json", 'w') as json_file:
            json.dump(listObj, json_file, 
                                indent=4,  
                                separators=(',',': '))
        