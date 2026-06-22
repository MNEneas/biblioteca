import sqlite3
import pessoa

conexao = sqlite3.connect("dados_livros.db")
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS livros(id INTEGER PRIMARY KEY ' \
'AUTOINCREMENT, titulo TEXT UNIQUE, emprestado INTEGER CHECK (emprestado IN (0, 1)))')

def cadastrar():
    titulo = input("Qual o nome do titulo do livro? ")
    cursor.execute('INSERT INTO livros(titulo, emprestado) values(?, ?)', (titulo, 0))

    conexao.commit()
    return print("Livro cadastrado")

def livro_disponiveis():
    try:
        cursor.execute('SELECT titulo FROM livros WHERE emprestado = 0')
        if cursor.fetchall != []:
            resultado = [item[0] for item in cursor.fetchall()]
            return resultado
        print("Nenhum livro foi encontrado")
        return
    except sqlite3.IntegrityError:
        print("Ocorreu um erro")

def emprestar():

    livro = input("Qual livro ira emprestar? ")
    if livro in livro_disponiveis():
        agraciado = input("Para quem ira emprestar? ")

        if agraciado in pessoa.pessoas_cadastradas():
            cursor.execute('UPDATE livros SET emprestado = 1 WHERE titulo = ?', (livro,))
            conexao.commit()
            print(f"Livro {livro} foi emprestado a {agraciado}.")
            return
        else:
            print("Não foi possivel emprestar o livro")
            return
    else:
        print("Livro não disponivel.")