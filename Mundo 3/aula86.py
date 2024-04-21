matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

valores_pares = []
terceira_coluna = []
segunda_linha = []

for i in range(3):
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i + 1}, {j + 1}]: "))
        matriz[i][j] = valor
        if valor % 2 == 0:
            valores_pares.append(valor)
        if j == 2:
            terceira_coluna.append(valor)
        if i == 1:
            segunda_linha.append(valor)

print("\nMatriz 3x3:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")  
    print()  

soma_pares = sum(valores_pares)
print("\nA soma de todos os valores pares digitados é:", soma_pares)

soma_terceira_coluna = sum(terceira_coluna)
print("A soma dos valores da terceira coluna é:", soma_terceira_coluna)

maior_segunda_linha = max(segunda_linha)
print("O maior valor da segunda linha é:", maior_segunda_linha)
