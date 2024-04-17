maiores_de_18 = 0
homens_cadastrados = 0
mulheres_menos_de_20 = 0

while True:
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M para masculino, F para feminino): ").upper()
    
    if idade > 18:
        maiores_de_18 += 1
    
    if sexo == 'M':
        homens_cadastrados += 1
    
    if sexo == 'F' and idade < 20:
        mulheres_menos_de_20 += 1
    
    continuar = input("Deseja cadastrar mais uma pessoa? (S para Sim, N para Não): ").upper()
    if continuar != 'S':
        break

print("A) Total de pessoas com mais de 18 anos:", maiores_de_18)
print("B) Total de homens cadastrados:", homens_cadastrados)
print("C) Total de mulheres com menos de 20 anos:", mulheres_menos_de_20)
