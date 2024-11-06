from contextlib import nullcontext
import psycopg2

from contato import Contato

class Conexao():
    def conexao(self):
            try:
                conn = psycopg2.connect(
                    dbname="Agenda",
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
            print(f"Erro ao inserir na tabela tabela: {e}")

   