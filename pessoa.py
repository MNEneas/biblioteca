import sqlite3

conexao = sqlite3.connect("dados_pessoas.db")
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS pessoas(id INTEGER PRIMARY KEY ' \
'AUTOINCREMENT, nome TEXT UNIQUE, email TEXT CHECK (email LIKE "%@%.%"))')

def cadastrar():
    nome = input("Qual o nome da pessoa? ")
    email = input("Qual o nome do email da pessoa? ")

    try:
        cursor.execute('INSERT INTO pessoas(nome, email) values(?, ?)', (nome, email))
        conexao.commit()

        return print("Pessoa cadastrada")
    except sqlite3.IntegrityError:
        return print("Ocorreu um erro com os dados passados")
def pessoas_cadastradas():
    cursor.execute('SELECT nome FROM pessoas')
    resultado = [item[0] for item in cursor.fetchall()]
    return resultado
