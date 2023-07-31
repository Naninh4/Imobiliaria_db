import sqlite3

conn = sqlite3.connect("imobiliaria.db")
cursor = conn.cursor()

# Função para atualizar qualquer campo
def update_table(tabela, id, campo, valor):
    cursor.execute(f"UPDATE {tabela} SET {campo} = '{valor}' WHERE id_{tabela} = {id}")
    conn.commit()

# Função para deletar linha
def delete_row(tabela, id):
    cursor.execute(f"DELETE FROM {tabela} WHERE id_{tabela} = {id}")
    conn.commit()

# Função para selecionar todas as linhas
def select_all(tabela):
    cursor.execute(f"SELECT * FROM {tabela}")
    return cursor.fetchall()

# Função para selecionar linha por ID
def select_by_id(tabela, id):
    cursor.execute(f"SELECT * FROM {tabela} WHERE id_{tabela} = {id}")
    return cursor.fetchone()

