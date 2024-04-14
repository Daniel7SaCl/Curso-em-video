while True:

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    
    print("[ 1 ] Somar")
    print("[ 2 ] Multiplicar")
    print("[ 3 ] Maior")
    print("[ 4 ] Novos números")
    print("[ 5 ] Sair do programa")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        resultado = valor1 + valor2
        print("A soma dos valores é:", resultado)
    elif escolha == 2:
        resultado = valor1 * valor2
        print("A multiplicação dos valores é:", resultado)
    elif escolha == 3:
        if valor1 > valor2:
            print("O maior valor é:", valor1)
        elif valor2 > valor1:
            print("O maior valor é:", valor2)
        else:
            print("Os valores são iguais.")
    elif escolha == 4:
        continue  
    elif escolha == 5:
        print("Saindo do programa...")
        break  
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
