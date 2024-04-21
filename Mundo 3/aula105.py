def mostrar_manual(comando):
    if comando == 'print':
        print("print(valor, ...):")
        print("    Exibe os valores passados como argumentos.")
    elif comando == 'input':
        print("input(prompt):")
        print("    Solicita ao usuário que insira um valor, exibe o prompt e retorna a entrada do usuário como uma string.")
    elif comando == 'len':
        print("len(s):")
        print("    Retorna o número de itens do objeto passado como argumento.")
    else:
        print("Comando não reconhecido.")

def main():
    print("=== Mini-Sistema de Ajuda Python ===")
    while True:
        comando = input("Digite o comando (ou 'FIM' para sair): ").strip()
        if comando.upper() == 'FIM':
            break
        else:
            mostrar_manual(comando)

    print("=== Programa encerrado ===")

if __name__ == "__main__":
    main()
