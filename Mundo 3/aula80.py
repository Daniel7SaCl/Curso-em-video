numeros = []

while True:
    numero = input("Digite um número (ou 'sair' para encerrar): ")
    if numero.lower() == "sair":
        break
    
    try:
        numero = float(numero)
    except ValueError:
        print("Por favor, digite um número válido.")
        continue
    
    numeros.append(numero)

quantidade_numeros = len(numeros)

numeros_ordenados = sorted(numeros, reverse=True)

if 5 in numeros:
    valor_5 = "está"
else:
    valor_5 = "não está"

print("A) Quantidade de números digitados:", quantidade_numeros)
print("B) Lista de valores, ordenada de forma decrescente:", numeros_ordenados)
print("C) O valor 5", valor_5, "na lista.")
