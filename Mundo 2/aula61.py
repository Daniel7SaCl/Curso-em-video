primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

contador = 0
termo_atual = primeiro_termo

while True:
    mostrar_mais = int(input("Quantos termos você gostaria de mostrar? (digite 0 para sair): "))
    
    if mostrar_mais == 0:
        print("Encerrando o programa...")
        break

    print("Os termos da PA são:")
    for _ in range(mostrar_mais):
        print(termo_atual, end=" ")
        termo_atual += razao
    print()  