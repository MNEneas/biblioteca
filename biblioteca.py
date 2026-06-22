import livros
import pessoa

print(f"{"="*30}")
print("1- Cadastrar um livro\n" \
"2- Cadastrar uma pessoa\n" \
"3- Emprestar livro\n" \
"4- Devolver livro\n")

opcao = input("Escolha uma opção: ")

match opcao:
    case "1":
        livros.cadastrar()

    case "2":
        pessoa.cadastrar()

    case "3":
        livros.emprestar()

    case _:
        print("Opção não aceita.")