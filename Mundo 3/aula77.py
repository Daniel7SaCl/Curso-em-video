
valores = 5
for i in range(5):
    valor = float(input(f"Digite o {i+1}º valor: "))
    valores.append(valor)

maior_valor = max(valores)
menor_valor = min(valores)
posicao_maior_valor = valores.index(maior_valor) + 1
posicao_menor_valor = valores.index(menor_valor) + 1

print("O maior valor digitado foi", maior_valor, "na posição", posicao_maior_valor)
print("O menor valor digitado foi", menor_valor, "na posição", posicao_menor_valor)
