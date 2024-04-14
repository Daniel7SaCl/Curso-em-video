soma = 0
contador = 0

while True:
    numero = int(input("Digite um número inteiro (ou 999 para parar): "))
    
    if numero == 999:
        break
    
    contador += 1
    soma += numero

print("Total de números digitados:", contador)
print("Soma dos números:", soma)
