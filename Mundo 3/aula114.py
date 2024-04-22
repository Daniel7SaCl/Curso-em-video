def opcao1():
    print("Você selecionou a Opção 1.")

def opcao2():
    print("Você selecionou a Opção 2.")

def opcao3():
    print("Você selecionou a Opção 3.")

def opcao4():
    print("Você selecionou a Opção 4.")

def mostrar_menu():
    print("=== MENU ===")
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Opção 3")
    print("4. Opção 4")
    print("0. Sair")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            opcao1()
        elif escolha == "2":
            opcao2()
        elif escolha == "3":
            opcao3()
        elif escolha == "4":
            opcao4()
        elif escolha == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")
