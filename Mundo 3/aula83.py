pessoas = []
while True:
    nome = input("Digite o nome da pessoa (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    peso = float(input("Digite o peso da pessoa em kg: "))
    pessoas.append((nome, peso))

print(f"\nForam cadastradas {len(pessoas)} pessoa(s).\n")

pessoas_ordenadas_por_peso = sorted(pessoas, key=lambda x: x[1], reverse=True)
print("Pessoas mais pesadas:")
for pessoa in pessoas_ordenadas_por_peso[:3]:
    print(f"Nome: {pessoa[0]}, Peso: {pessoa[1]} kg")

print("\nPessoas mais leves:")
pessoas_ordenadas_por_peso = sorted(pessoas, key=lambda x: x[1])
for pessoa in pessoas_ordenadas_por_peso[:3]:
    print(f"Nome: {pessoa[0]}, Peso: {pessoa[1]} kg")
