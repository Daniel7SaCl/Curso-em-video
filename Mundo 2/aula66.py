while True:
    numero = int(input("Digite um número para ver sua tabuada (digite um número negativo para parar): "))
    
    if numero < 0:
        print("Programa encerrado.")
        break

    print("Tabuada de", numero, ":")
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)