import sqlite3 as lite

# Criando a conexão
conn = lite.connect('clientes.db')


# Inserir informações
def inserir_info(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO formulario(nome, cpf, email, telefone, dia_em, estado, assunto) VALUES (?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)


# Acessar informações
def exibir_info():
    lista = []
    with conn:
        cur = conn.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        info = cur.fetchall()

        for i in info:
            lista.append(i)
    return lista

'''
# Atualizar informações
with conn:
    cur = conn.cursor()
    query = "UPDATE formulario SET nome=? WHERE id =?"
    cur.execute(query, lista)

# Deletar informações
with (conn):
    cur = conn.cursor()
    query = "DELETE FROM formulario WHERE id =?"
    cur.execute(query, lista)
'''