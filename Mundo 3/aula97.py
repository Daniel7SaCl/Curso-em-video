def contador(inicio, fim, passo):
    print(f"Contagem de {inicio} até {fim}, de {passo} em {passo}:")
    if passo > 0:
        for i in range(inicio, fim + 1, passo):
            print(i, end=" ")
    elif passo < 0:
        for i in range(inicio, fim - 1, passo):
            print(i, end=" ")
    print("\n")

contador(1, 10, 1)

contador(10, 0, -2)

inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))
passo = int(input("Digite o passo: "))
contador(inicio, fim, passo)
