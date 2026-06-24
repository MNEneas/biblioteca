import sqlite3
import pessoa

conexao = sqlite3.connect("dados_livros.db")
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS livros(id INTEGER PRIMARY KEY ' \
'AUTOINCREMENT, titulo TEXT UNIQUE, emprestado INTEGER CHECK (emprestado IN (0, 1)))')

def cadastrar():
    try:
        titulo = input("Qual o nome do titulo do livro? ")
        cursor.execute('INSERT INTO livros(titulo, emprestado) values(?, ?)', (titulo, 0))

        conexao.commit()
        return print("Livro cadastrado")
    except sqlite3.IntegrityError:
        print("Ocorreu um erro")

def disponibilidade_livros(disponivel):
    cursor.execute('SELECT titulo FROM livros WHERE emprestado = ?', (disponivel,))
    lista = [item[0] for item in cursor.fetchall()]
    return lista

def emprestar():
    try:
        livro = input("Qual livro ira emprestar? ")
        if livro in disponibilidade_livros(0):
            agraciado = input("Para quem ira emprestar? ")

            if agraciado in pessoa.pessoas_cadastradas():

                pessoa.pegar_livro(livro, agraciado)

                cursor.execute('UPDATE livros SET emprestado = 1 WHERE titulo = ?', (livro,))
                conexao.commit()
                return
            else:
                print("Não foi possivel emprestar o livro")
                return
        else:
            print("Livro não disponivel.")
    except sqlite3.IntegrityError:
        print("Ocorreu um erro")

def devolver():
    try:
        livro = input("Qual livro ira devolver? ")
        if livro in disponibilidade_livros(1):
            pessoa.devolver_livro(livro)
            cursor.execute('UPDATE livros SET emprestado = 0 WHERE titulo = ?', (livro,))
            conexao.commit()
            return
        else:
            print("Esse livro não foi emprestado")
            return
    except sqlite3.IntegrityError:
        print("Ocorreu um erro")