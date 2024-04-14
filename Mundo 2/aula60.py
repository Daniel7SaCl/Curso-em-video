primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

contador = 0
termo_atual = primeiro_termo

print("Os 10 primeiros termos da PA são:")
while contador < 10:
    print(termo_atual, end=" ")
    termo_atual += razao
    contador += 1
