import json
from baixa.baixa import Baixa
from cadastro.cadastro import CadastroGeral
from banco.imprimirNota import ImprimirNota
imprimirNota = ImprimirNota()
print('''Sejá Bem Vindo ao Supermecado JN!''')

while True:
    print('''========== Opções Iniciais==========''')
    print('''
    [1] - Baixa de Produto
    [2] - Adicionar Produto
    [3] - Cadastrar cliente
    [4] - Gerar Notas das vendas
    [5] - Encerrar Caixa.
    ''')

    escolha = int(input(":"))
    if(escolha == 1):
        Baixa.autenticator()
    elif(escolha == 2):
        CadastroGeral.cadastroDoProduto()
    elif(escolha == 3):
        CadastroGeral.cadastroCliente()
    elif(escolha == 4):
        imprimirNota.impressao()
    elif(escolha == 5):
        break
    else:
        print("Opção não encontrada por favor digitá novamente o numero da opção!!!")