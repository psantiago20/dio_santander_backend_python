import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def criar_tabela(cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    conexao.commit()


def inserir_registro(conexao, cursor, nome, email):
    data = ("Simba", "simba@teste.com")
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()


def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE ID=?;", data)
    conexao.commit()


def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE ID=?;", data)
    conexao.commit()


# atualizar_registro(conexao, cursor, 'Pedro Santiago', 'pedro@teste.com', 1)
# atualizar_registro(conexao, cursor, 'Simba Nenê', 'simba_nene@teste.com', 2)
# excluir_registro(conexao, cursor, 1)


def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    conexao.commit()


def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()


def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")


clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))


cliente = recuperar_cliente(cursor, 2)
print(dict(cliente))
print(cliente["id"], cliente["nome"], cliente["email"])


print(f'Seja bem vindo ao sistema {cliente["nome"]}')


# dados = [
#     ('Pedro', 'pedro@teste.com'),
#     ('Bento', 'bento_bebe@teste.com'),
#     ('Chappie', 'chappie@teste.com')
# ]
# inserir_muitos(conexao, cursor, dados)
