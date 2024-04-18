# Lista para armazenar os valores numéricos
valores = []

# Ler 5 valores numéricos
for i in range(5):
    valor = float(input(f"Digite o {i+1}º valor: "))
    valores.append(valor)

# Encontrar o maior e o menor valor e suas posições na lista
maior_valor = max(valores)
menor_valor = min(valores)
posicao_maior_valor = valores.index(maior_valor) + 1
posicao_menor_valor = valores.index(menor_valor) + 1

# Mostrar os resultados
print("O maior valor digitado foi", maior_valor, "na posição", posicao_maior_valor)
print("O menor valor digitado foi", menor_valor, "na posição", posicao_menor_valor)
