import sqlite3

# Conecta ao banco de dados ou cria um novo se não existir
con = sqlite3.connect('teste_sqlite.db')
# Cria um cursor para interagir com o banco de dados
cursor = con.cursor()


# Exemplo: criar uma tabela
cursor.execute("CREATE TABLE IF NOT EXISTS contatos(nome TEXT, endereco TEXT, telefone TEXT)")

# Inserir dados na tabela
cursor.execute("INSERT INTO contatos VALUES ('João', 'Rua 123', '123456789')")
cursor.execute("INSERT INTO contatos VALUES ('Maria', 'Avenida XYZ', '987654321')")

# Executa a consulta para selecionar todos os registros da tabela 'contatos'
cursor.execute("SELECT * FROM contatos")

# Retorna todas as linhas resultantes
linhas_resultantes = cursor.fetchall()

# Exibe as linhas resultantes
for linha in linhas_resultantes:
    print(linha)

"""
# Retorna uma linha resultante
linha_resultante = cursor.fetchone()

# Exibe a linha resultante (pode ser None se não houver registros)
print(linha_resultante)

"""
# Exemplo: apagar todos os dados da tabela
cursor.execute("DELETE FROM contatos")

con.commit()  # Salva as mudanças no banco de dados
con.close()   # Fecha a conexão com o banco de dados


