soma_idades = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ""
mulheres_menos_20 = 0

for i in range(4):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M/F): ").upper()


    soma_idades += idade


    if sexo == "M" and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

media_idades = soma_idades / 4
print("Média de idade do grupo:", media_idades)
print("Nome do homem mais velho:", nome_homem_mais_velho)
print("Quantidade de mulheres com menos de 20 anos:", mulheres_menos_20)