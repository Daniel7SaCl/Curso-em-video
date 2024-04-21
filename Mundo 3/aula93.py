pessoas = []
soma_idades = 0

quantidade_pessoas = int(input("Quantas pessoas serão cadastradas? "))

for i in range(1, quantidade_pessoas + 1):
    pessoa = {}
    pessoa['nome'] = input(f"Digite o nome da {i}ª pessoa: ")
    pessoa['sexo'] = input(f"Digite o sexo da {i}ª pessoa (M/F): ").upper()
    pessoa['idade'] = int(input(f"Digite a idade da {i}ª pessoa: "))
    pessoas.append(pessoa)
    soma_idades += pessoa['idade']

media_idade = soma_idades / quantidade_pessoas

mulheres = []
acima_da_media = []

for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    if pessoa['idade'] > media_idade:
        acima_da_media.append(pessoa['nome'])

print(f"\nForam cadastradas {quantidade_pessoas} pessoas.")
print(f"A média de idade das pessoas cadastradas é: {media_idade:.1f} anos.")
print("Lista de mulheres:", mulheres)
print("Lista de pessoas com idade acima da média:", acima_da_media)
