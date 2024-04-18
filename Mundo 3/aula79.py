valores = []

for i in range(5):
    valor = float(input(f"Digite o {i+1}º valor: "))
    
    if len(valores) == 0 or valor >= valores[-1]:
        valores.append(valor)
    else:
        for j in range(len(valores)):
            if valor <= valores[j]:
                valores.insert(j, valor)
                break

print("Lista ordenada:", valores)