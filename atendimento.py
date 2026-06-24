import biblioteca
import pessoa

while True:
    print(f"{"="*30}")
    print("1- Cadastrar um livro\n" \
    "2- Cadastrar uma pessoa\n" \
    "3- Emprestar livro\n" \
    "4- Devolver livro\n" \
    "0- Sair\n")

    opcao = input("Escolha uma opção: ")
    match opcao:
        case "1":
            biblioteca.cadastrar()

        case "2":
            pessoa.cadastrar()

        case "3":
            biblioteca.emprestar()

        case "4":
            biblioteca.devolver()

        case "0":
            break

        case _:
            print("Opção não aceita.")