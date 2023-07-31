import sqlite3
import os
from gets import *
from sets import *
from funções import *
# Conecta ao banco de dados (cria um novo se não existir)

conn = sqlite3.connect("imobiliaria.db")
cursor = conn.cursor()

# Interface do terminal

def main():
    print("-----    SISTEMA DE GERENCIAMENTO IMOBILIÁRIO   -----")

    while True:
        menu_principal()
        # print("1 - Atualizar campo")
        # print("2 - Deletar linha")
        # print("3 - Selecionar todas as linhas")
        # print("4 - Selecionar linha por ID")
        # print("5 - Inserir dados em uma tabela")
        # print("0 - Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            menu_tables()
            t = input("Em qual tabela deseja fazer alteração?: ")

            tabela = t.strip().lower()
            print(tabela)
            select_campos_all(tabela)
            id =  int(input("Informe o id da linha onde a alteração deve ser feita: "))

            col =  input("Informe a coluna que deseja realizar a alteração: ")
            valor =  input("Informe a alteração: ")
            update_table(tabela, id, col, valor)
            print("\nValor alterado com sucesso! \n")
        if opcao == 2:
            menu_tables()
            t = input("Em qual tabela deseja fazer alteração?: ")

            tabela = t.strip().lower()
            select_campos_all(tabela)
            id =  int(input("Informe o id da linha que deseja deletar: "))
            delete_row(tabela, id)
            print("\nValor alterado com sucesso! \n")
        if opcao == 3:
            menu_tables()
            t = input("Qual tabela deseja vizualizar todas as linhas? ")
            tabela = t.strip().lower()
            print("Tabela: " , tabela.upper())
            select_campos_all(tabela)
            print("Operação realizada com sucesso!")
        if opcao == 4: 
            menu_tables()
            t = input("De qual tabela deseja vizualizar a linha? ")
            tabela = t.strip().lower()
            id = int(input("Informe o ID da linha: "))
            print("Tabela: " , tabela.upper())
            select_campo_id(tabela, id)
            print("Operação realizada  com sucesso!\n")
        if opcao == 5:
            menu_tables()
            t = input("Em qual tabela deseja inserir os dados? ")
            tabela = t.strip().lower()
            gerenciador(tabela)
main()
                
# Fecha conexão com o banco de dados


