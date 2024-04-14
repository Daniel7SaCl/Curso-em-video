soma = 0
contador = 0
maior = menor = None

while True:
    numero = int(input("Digite um número inteiro: "))
    
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero
    
    contador += 1
    soma += numero
    
    
    continuar = input("Deseja continuar? (S/N): ").strip().upper()
    if continuar != 'S':
        break

if contador > 0:
    
    media = soma / contador
    
    print(f"Média dos números digitados: {media}")
    print(f"Maior número digitado: {maior}")
    print(f"Menor número digitado: {menor}")
else:
    print("Nenhum número foi digitado.")
