valores_unicos = []

while True:
    valor = input("Digite um valor numérico (ou 'sair' para encerrar o programa): ")

    if valor.lower() == "sair":
        break

    try:
        valor = float(valor)
    except ValueError:
        print("Por favor, digite um valor numérico válido.")
        continue
    
    if valor not in valores_unicos:
        valores_unicos.append(valor)

valores_unicos.sort()

print("Valores únicos digitados (em ordem crescente):", valores_unicos)