import sqlite3
from datetime import date, timedelta

conexao = sqlite3.connect("dados_pessoas.db")
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS pessoas(id INTEGER PRIMARY KEY ' \
'AUTOINCREMENT, nome TEXT UNIQUE, livro TEXT, data TEXT, email TEXT CHECK (email LIKE "%@%.%"))')

def cadastrar():
    nome = input("Qual o nome da pessoa? ")
    email = input("Qual o nome do email da pessoa? ")

    try:
        cursor.execute('INSERT INTO pessoas(nome, livro, data, email)' \
                       'values(?, ?, ?, ?)', (nome, None, None, email))
        conexao.commit()

        return print("Pessoa cadastrada")
    except sqlite3.IntegrityError:
        return print("Ocorreu um erro com os dados passados")

def pessoas_cadastradas():
    cursor.execute('SELECT nome FROM pessoas')
    resultado = [item[0] for item in cursor.fetchall()]
    return resultado

def pegar_livro(livro, pessoa):
    data_hoje = date.today()
    data_entega = (data_hoje + timedelta(days=10)).strftime("%d/%m/%Y")

    cursor.execute('UPDATE pessoas SET livro = ?, data = ? WHERE nome = ?', (livro, data_entega, pessoa))
    conexao.commit()

    print(f"Você pegou o livro {livro}, deve devolve-lo {data_entega}")
    return

def devolver_livro(livro):
    cursor.execute('SELECT data FROM pessoas WHERE livro = ?', (livro,))
    data_entrega = cursor.fetchone()

    print(f"Você entregou o livro {livro}, a data de entrega limite é {data_entrega[0]}")

    cursor.execute('UPDATE pessoas SET data = ? WHERE livro = ?', (None, livro))
    conexao.commit()
