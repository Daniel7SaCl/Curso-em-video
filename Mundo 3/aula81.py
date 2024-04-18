numeros = []
pares = []
impares = []

while True:
    numero = input("Digite um número (ou 'sair' para encerrar): ")
    
    if numero.lower() == "sair":
        break
    
    try:
        numero = int(numero)
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números digitados:", numeros)
print("Valores pares:", pares)
print("Valores ímpares:", impares)