import sqlite3

conn  = sqlite3.connect("imobiliaria.db")

cursor = conn.cursor()

sql = "SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';"

teste = cursor.execute(sql)
name_tables = []
matriz = list(teste)

linha =  len(matriz)
coluna =  len(matriz[0])

for x in range(0,linha):
    for e in range(0, coluna):
        if e == 0:
            name_tables.append(matriz[x][e])

print(name_tables)