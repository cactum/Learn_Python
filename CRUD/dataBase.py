import sqlite3 as lite

con = lite.connect('clientes.db')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, cpf TEXT, email TEXT, "
                "telefone TEXT, dia_em DATE, estado TEXT, assunto TEXT)")

