import json

class ImprimirNota():
   def impressao(self):
        with open("C:\\Users\\Cicero\\Videos\\projeto-rec\\banco\\notaFiscal.json", encoding='utf-8') as jsonFile:
                user = json.load(jsonFile)

        listWrite = list()
            
        Topo = ("========= Nota =========  \n")
        listWrite.append(Topo)
            
        for valor in range(len(user)):
            nome=f"Nome Do Cliente   -------------------- {str(user[valor]['nome_do_cliente'])} \n"
            pedidoCliente=f"Pedido_do_cliente --------------------- {str(user[valor]['pedido_do_cliente'])} \n"
            valorCliente= f"Valor_pago  --------------------------- {str(user[valor]['valor_pago']) } \n"
            troco= f"Troco   --------------------- {str(user[valor]['troco'])} \n"
            data=  f"Data ---------------------------------- {str(user[valor]['data'])} \n"
            fim="========================================================= \n" 
                
            listWrite.append(nome)
            listWrite.append(pedidoCliente)
            listWrite.append(valorCliente)
            listWrite.append(troco)
            listWrite.append(data)
            listWrite.append(fim)
        with open("impressaoNotaFiscal.txt","a") as impressao:
            impressao.writelines(listWrite)