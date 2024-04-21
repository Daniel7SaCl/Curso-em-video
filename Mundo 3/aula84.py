valores = [[], []] 

for _ in range(7):
    valor = int(input("Digite um valor numérico: "))
    if valor % 2 == 0:
        valores[0].append(valor)  
    else:
        valores[1].append(valor)  

valores[0].sort()
valores[1].sort()

print("Valores pares:", valores[0])
print("Valores ímpares:", valores[1])
