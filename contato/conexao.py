from contextlib import nullcontext
import psycopg2
class Contato():
    id: int
    nome: str
    telefone: str
    endereco: str
    def __init__(self, nome: str, telefone: str, endereco: str):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

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



    def insert_contato(self, cont: Contato):
        
        try:
            with conn.cursor() as cursor:
                query = f"""  INSERT INTO contato (nome,telefone, endereco) VALUES ('{cont.nome}','{cont.telefone}', '{cont.endereco}')"""
                cursor.execute(query)
                query = f""" SELECT id FROM contato WHERE contato.nome = '{cont.nome}' """
                cursor.execute(query)
                id = cursor.fetchall()
                print(id)
                print("Objeto criado")
                conn.commit() 
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")

   