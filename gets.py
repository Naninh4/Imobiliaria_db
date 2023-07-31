from funções import *

# section menus
def menu_principal():
    print("1 - Atualizar campo")
    print("2 - Deletar linha")
    print("3 - Selecionar todas as linhas")
    print("4 - Selecionar linha por ID")
    print("5 - Insirir dados em uma tabela")
    print("0 - Sair")


def menu_tables():
    print("---  TABELAS DISPONÍVEIS  ---")
    print("1 - Corretor ")
    print("2 - Cliente ")
    print("3 - Cidade ")
    print("5 - Imóvel ")
    print("6 - Pagamentos ")
    print("0 - Sair ")


# section selects
def select_campo_id(tabela,id):

    colunas = get_campos_table(tabela)
    colunas.insert(0,"Id")   
    linha = select_by_id(tabela,id)
    col = 0
    print("Resultado da consulta: \n")
    for coluna in linha:
        print(f"- {colunas[col].capitalize()}: {coluna}", end=" | ")
        col+=1


def select_campos_all(tabela):
    print(f"| Items disponíveis: \n".upper())
    objetos = select_all(tabela)
    colunas = get_campos_table(tabela)
    colunas.insert(0,"Id")
    table = []
    for objeto in objetos:
        table.append(list(objeto))
    for linha in table:
        print("- ", end="")
        for coluna in range(0,len(colunas)):
                print(f"{colunas[coluna].capitalize()}: ", linha[coluna], end=" | ")
        print("\n")

def get_campos_table(tabela):
    
    cursor = conn.cursor()

    sql = f"PRAGMA table_info({tabela.lower().strip()})" #consultando informções de criação da tabela

    names = cursor.execute(sql)
    #retornando um objeto referente ao script de criação da tabela "<sqlite3.Cursor object at 0x000002B417D17D40>"
    # Como é um objeto, temos que destrinxar suas informações 

    matriz = []

    for x in names:
        matriz.append(list(x)) 
        # cada elemento do objeto, que nesse caso é cada atributo da tabelaa deve ser adicionado em formato de lista
        # assim gerando uma matriz (uma lista de listas)  
    # print(matriz)

    # a matriz gerada acima ficará mais ou menos assim:
    #[[0, 'id_cidade', 'INTEGER', 0, None, 1], 
    # [1, 'nome', 'VARCHAR', 1, None, 0], 
    # [2, 'estado', 'VARVHAR', 1, None, 0]]

    #feito isso, nota-se que o nome dos campos estão sempre na posição [n][1] 
    # ou seja, em qualquer que seja a linha  ele sempre está na sua posição interna 1. 

    #então vamos criar uma lista que receba os nomes dos campos
    nome_campos = []

    #agr que já sabemos onde podemos consultar os nomes dos campos da tabela
    # vamos acessá-los e guardá-los para aplicações futuras

    # Primeiro vamos criar uma variável (linhas) para identificar quantos atributos (campos) 
    # existem na tabela consultada, já que a quantidade de items na matriz tbm indica a quanti-
    #dade de campos dessa tabela.

    linhas = len(matriz)

    # logo após cria-se uma variável para receber quantos itens há em cada linha da matriz, ou seja, 
    # a quantidade de colunas.

    colunas = len(matriz[0])


    for linha in range(0,linhas):
        #percorrendo as linhas da matriz
        for coluna in range(0,colunas):
            # percorrendo as colunas da matriz
            if coluna == 1:
                # como sabemos que o nome do campo sempre vai estar na coluna 1 de qualquer linha
                # sempre que a coluna for 1 vamos guardar o seu valor na variável nome_campos
                if matriz[linha][coluna] != f"id_{tabela}":
                    nome_campos.append(matriz[linha][coluna])
    return nome_campos
