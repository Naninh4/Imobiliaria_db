from contextlib import nullcontext
from select import select
import psycopg2

from contato import Contato

class Conexao():
    def conexao(self):
            try:
                conn = psycopg2.connect(
                    dbname="postgres",
                    user="postgres",
                    password="postgres",
                    host="localhost",
                    port="5432"
                )
                print("funfou")
                return conn
            except Exception as e:
                print(f"Erro ao conectar ao banco de dados: {e}")
                return None
    #



    def insert_contato(conn, cont: Contato):
        try:
            with conn.cursor() as cursor:
                query = f"""  INSERT INTO contato (nome,telefone, endereco) VALUES ('{cont.nome}','{cont.telefone}', '{cont.endereco}')"""
                cursor.execute(query)
                conn.commit()
                # Definir o comprimento máximo de cada coluna, baseado nos dados inseridos

                nome_len = max(len(cont.nome), len("Nome"))
                telefone_len = max(len(cont.telefone), len("Telefone"))
                endereco_len = max(len(cont.endereco), len("Endereço"))
                
                # Criar os separadores da tabela com base nos comprimentos das colunas
                separator = "+" + "-" * (nome_len + 2) + "+" + "-" * (telefone_len + 2) + "+" + "-" * (endereco_len + 2) + "+"
                
                # Exibir a tabela com formatação dinâmica
                print(separator)
                print(f"| {'Nome'.ljust(nome_len)} | {'Telefone'.ljust(telefone_len)} | {'Endereço'.ljust(endereco_len)} |")
                print(separator)
                print(f"| {cont.nome.ljust(nome_len)} | {cont.telefone.ljust(telefone_len)} | {cont.endereco.ljust(endereco_len)} |")
                print(separator)

        except Exception as e:
            print(f"Erro ao inserir na tabela: {e}")

    def remover_contato(conn, id: int):
        try:
            with  conn.cursor() as cursor:
                query = f""" DELETE FROM contato WHERE contato.id = {id}; """
                cursor.execute(query)
                print("Objeto removido com sucesso!")
                conn.commit()
        except Exception as e:
                print(f"Erro ao remover o objeto: {e}")
    
    
    def select_contato_by_id(conn, id: int):
        try:
            with  conn.cursor() as cursor:
                query = f""" SELECT * FROM contato WHERE contato.id = {id}"""
                cursor.execute(query)
                rows: Contato = cursor.fetchall()
                for cont in rows:
                    id_len = max(len(str(cont[0])), len("#"))
                    nome_len = max(len(cont[1]), len("Nome"))
                    telefone_len = max(len(cont[2]), len("Telefone"))
                    endereco_len = max(len(cont[3]), len("Endereço"))
                    
                    # Criar os separadores da tabela com base nos comprimentos das colunas
                    separator = "+" + "-" * (id_len + 2) + "+" + "-" * (nome_len + 2) + "+" + "-" * (telefone_len + 2) + "+" + "-" * (endereco_len + 2) + "+"
                    
                    # Exibir a tabela com formatação dinâmica
                    print(separator)
                    print(f"| {'#'.ljust(id_len)} | {'Nome'.ljust(nome_len)} | {'Telefone'.ljust(telefone_len)} | {'Endereço'.ljust(endereco_len)} |")
                    print(separator)
                    print(f"| {str(cont[0]).ljust(id_len)} | {cont[1].ljust(nome_len)} | {cont[2].ljust(telefone_len)} | {cont[3].ljust(endereco_len)} |")
                    print(separator)
                    
        except Exception as e:
            print(f"Erro ao remover o objeto: {e}")



    def alterar_contato(conn, cont: Contato ):
        try:
            with  conn.cursor() as cursor:
                query = f""" UPDATE contato SET nome = '{cont.nome}', telefone = '{cont.telefone}', endereco = '{cont.endereco}' WHERE  contato.id = {cont.id}; """
                cursor.execute(query)
                conn.commit()
                print("Objeto alterado!")  
        except Exception as e:
                print(f"Erro ao selecionar  o objeto: {e}")
    
    
    def listar_contatos(conn):
        try:
            with  conn.cursor() as cursor:
                query = f""" SELECT * FROM contato """
                cursor.execute(query)
                rows: Contato = cursor.fetchall()
                for cont in rows:
                    id_len = max(len(str(cont[0])), len("#"))
                    nome_len = max(len(cont[1]), len("Nome"))
                    telefone_len = max(len(cont[2]), len("Telefone"))
                    endereco_len = max(len(cont[3]), len("Endereço"))
                    
                    # Criar os separadores da tabela com base nos comprimentos das colunas
                    separator = "+" + "-" * (id_len + 2) + "+" + "-" * (nome_len + 2) + "+" + "-" * (telefone_len + 2) + "+" + "-" * (endereco_len + 2) + "+"
                    
                    # Exibir a tabela com formatação dinâmica
                    print(separator)
                    print(f"| {'#'.ljust(id_len)} | {'Nome'.ljust(nome_len)} | {'Telefone'.ljust(telefone_len)} | {'Endereço'.ljust(endereco_len)} |")
                    print(separator)
                    print(f"| {str(cont[0]).ljust(id_len)} | {cont[1].ljust(nome_len)} | {cont[2].ljust(telefone_len)} | {cont[3].ljust(endereco_len)} |")
                    print(separator)

        except Exception as e:
                print(f"Erro ao remover o objeto: {e}")

