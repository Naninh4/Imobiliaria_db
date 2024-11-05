from conexao import Conexao
import psycopg2


conn = Conexao().conexao()


try:
    with conn.cursor() as cursor:
        query = """ 
        CREATE TABLE contato(
            id SERIAL PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            telefone VARCHAR(11) NOT NULL,
            endereco VARCHAR
        );
        """
        cursor.execute(query)
        print("Tabela criada com sucesso!")
        conn.commit() 

except Exception as e:
    print(f"Erro ao criar tabela: {e}")
