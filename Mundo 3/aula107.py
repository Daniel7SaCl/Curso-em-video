def aumentar(preco, taxa):
    return preco * (1 + taxa / 100)

def diminuir(preco, taxa):
    return preco * (1 - taxa / 100)

def dobro(preco):
    return preco * 2

def metade(preco):
    return preco / 2

def moeda(preco):
    return f'R${preco:.2f}'.replace('.', ',')

preco = float(input("Digite o preço: "))

print(f"Preço original: {moeda(preco)}")
print(f"Preço com 10% de aumento: {moeda(aumentar(preco, 10))}")
print(f"Preço com 15% de desconto: {moeda(diminuir(preco, 15))}")
print(f"Dobro do preço: {moeda(dobro(preco))}")
print(f"Metade do preço: {moeda(metade(preco))}")
