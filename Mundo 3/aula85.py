matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para a posição [{i + 1}, {j + 1}]: "))

print("\nMatriz 3x3:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")  #
    print()  