numero = int(input("Digite um número para calcular o fatorial: "))

fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print(f"{numero}! =", end=" ")
for i in range(numero, 0, -1):
    if i != 1:
        print(i, "x", end=" ")
    else:
        print(i, "=", fatorial)