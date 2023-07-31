import sqlite3

# Conecta ao banco de dados (cria um novo se não existir)
conn = sqlite3.connect("imobiliaria.db")
cursor = conn.cursor()


# # Cria a tabela imóveis
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS cidade (
#     id_cidade INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome VARCHAR NOT NULL,
#     estado VARCHAR NOT NULL

# );
# """)

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS cliente (
#     id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome VARCHAR NOT NULL,
#     email VARVHAR NOT NULL,
#     id_cidade INT,
#     FOREIGN KEY (id_cidade) REFERENCES cidade (id_cidade)
# );
# """)

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS corretor (
#     id_corretor INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome VARCHAR NOT NULL,
#     cpf VARCHAR NOT NULL,
#     email VARCHAR NOT NULL

# );
# """)



# cursor.execute("""
# CREATE TABLE IF NOT EXISTS imovel (
#     id_imovel INTEGER PRIMARY KEY AUTOINCREMENT,
#     logradouro VARCHAR NOT NULL,
#     numero INTEGER NOT NULL,
#     bairro VARCHAR NOT NULL,
#     id_cidade VARCHAR NOT NULL,
#     FOREIGN KEY (id_cidade) REFERENCES cidade (id_cidade)

# );""")

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS aluguel(
#     id_aluguel INTEGER PRIMARY KEY AUTOINCREMENT,
#     data_inicio VARCHAR NOT NULL,
#     valor DOUBLE NOT NULL,
#     id_cliente INT NOT NULL,
#     id_corretor INT NOT NULL,
#     id_imovel INT NOT NULL

# );
# """)
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS pagamento (
#     id_pagamento INTEGER PRIMARY KEY AUTOINCREMENT,
#     data_pagamento VARCHAR NOT NULL,
#     observacao VARCHAR NOT NULL,
#     valor FLOAT NOT NULL,
#     id_aluguel INT,
#     FOREIGN KEY (id_aluguel) REFERENCES aluguel (id_aluguel)
# );
# """)


# # Encerra a conexão
# conn.close()
