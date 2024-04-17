soma = 0
contador = 0

while True:
    numero = int(input("Digite um número inteiro (999 para parar): "))
    
    if numero == 999:
        break
    
    soma += numero
    contador += 1

print("Você digitou", contador, "números.")
print("A soma deles é:", soma)
