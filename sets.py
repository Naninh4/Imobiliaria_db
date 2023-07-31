from gets import *


def gerenciador(tabela):
    if tabela ==  "corretor":
        insert_corretor
    if tabela == "cidade":
        insert_cidade()
    if tabela == "imoveis":
        insert_imoveis()
    if tabela ==  "pagamentos":
        insert_pagamentos()
    if tabela == "cliente":
        insert_cliente()
    if tabela ==  "aluguel":
        insert_aluguel()
    
def insert_corretor():
    tabela = "corretor"
    values = []
    campos_n = get_campos_table(tabela)
    for atributo in campos_n:
    #mostrando
        value = input(f"- {atributo.capitalize()}: ")
        values.append(f"'{value}'") 
                
    valores =  ",".join(values)
    campos = ','.join(campos_n)
    insert_data(tabela,campos, valores)

def insert_cidade():
    tabela = "cidade"
    values = []
    campos_n = get_campos_table(tabela)
    for atributo in campos_n:
    #mostrando
        value = input(f"- {atributo.capitalize()}: ")
        values.append(f"'{value}'") 
                
    valores =  ",".join(values)
    campos = ','.join(campos_n)
    insert_data(tabela, campos, valores)

def insert_imoveis():
    tabela = "imovel"
    values = []
    campos_n = get_campos_table(tabela)

    for atributo in campos_n:
    #mostrando
        if "id_cidade" in atributo:

            opcao = int(input("1 - Selecionar cidade \n2 - Cadastrar nova cidade\n Opção: "))
            if opcao == 1:
                select_campos_all(tabela="cidade")
                value = input(f"- {atributo.capitalize()}: ")
                values.append(f"'{value}'")
            elif opcao == 2:
                print("-- CADASTRO DE CIDADE --")
                insert_cidade()
                select_campos_all(tabela="cidade")
                value = input(f"- {atributo.capitalize()}: ")
                values.append(f"'{value}'")
        else:
            value = input(f"- {atributo.capitalize()}: ")
            values.append(f"'{value}'") 
                
    valores =  ",".join(values)
    campos = ','.join(campos_n)

    insert_data(tabela,campos, valores)

def insert_aluguel():
    tabela = "aluguel"
    values = []
    campos_n = get_campos_table(tabela)
    for atributo in campos_n:
        for atributo in campos_n:
            if "id_imovel" in atributo:
                opcao = int(input("1 - Selecionar cidade \n2 - Cadastrar nova cidade\n Opção: "))
                if opcao == 1:
                    value = input(f"- {atributo.capitalize()}: ")
                    values.append(f"'{value}'")
                elif opcao == 2:
                    print("-- CADASTRO DE CIDADE --")
                    insert_cidade()
                    value = input(f"- {atributo.capitalize()}: ")
                    values.append(f"'{value}'")
            else:
                value = input(f"- {atributo.capitalize()}: ")
                values.append(f"'{value}'")      
    valores =  ",".join(values)
    campos = ','.join(campos_n)

    insert_data(tabela,campos, valores)

def insert_cliente():
    tabela = "cidade"
    values = []
    campos_n = get_campos_table(tabela)
    for atributo in campos_n:
    #mostrando
        if "id_cidade" in atributo:
            opcao = int(input("1 - Selecionar cidade \n2 - Cadastrar nova cidade\n Opção: "))
            if opcao == 1:
                value = input(f"- {atributo.capitalize()}: ")
                values.append(f"'{value}'")
            elif opcao == 2:
                print("-- CADASTRO DE CIDADE --")
                insert_cidade()
                value = input(f"- {atributo.capitalize()}: ")
                values.append(f"'{value}'")
        else:
            value = input(f"- {atributo.capitalize()}: ")
            values.append(f"'{value}'") 
                
    valores =  ",".join(values)
    campos = ','.join(campos_n)

    insert_data(tabela,campos, valores)

def insert_pagamentos():
    tabela = "pagamentos"
    values = []
    campos_n = get_campos_table(tabela)
    for atributo in campos_n:
    #mostrando
        value = input(f"- {atributo.capitalize()}: ")
        values.append(f"'{value}'") 
                
    valores =  ",".join(values)
    campos = ','.join(campos_n)
    insert_data(tabela, campos, valores)
    
# Função para inserir dados na tabela
def insert_data(tabela,campos,valores):
                
    print(f"\n {tabela} CADASTRADA! \n")    
    insert = (f"INSERT INTO {tabela} ({campos}) VALUES ({valores});")
    print(insert)
    cursor.execute(insert)
    conn.commit()
