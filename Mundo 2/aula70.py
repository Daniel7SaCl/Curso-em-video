valor_saque = int(input("Digite o valor a ser sacado (em múltiplos de R$1): "))

cedulas_50 = 0
cedulas_20 = 0
cedulas_10 = 0
cedulas_1 = 0

while valor_saque > 0:
    if valor_saque >= 50:
        cedulas_50 += 1
        valor_saque -= 50
    elif valor_saque >= 20:
        cedulas_20 += 1
        valor_saque -= 20
    elif valor_saque >= 10:
        cedulas_10 += 1
        valor_saque -= 10
    else:
        cedulas_1 += 1
        valor_saque -= 1

print("Quantidade de cédulas de R$50:", cedulas_50)
print("Quantidade de cédulas de R$20:", cedulas_20)
print("Quantidade de cédulas de R$10:", cedulas_10)
print("Quantidade de cédulas de R$1:", cedulas_1)
