def aumentar(preco, taxa, formatar=False):
    resultado = preco * (1 + taxa / 100)
    return moeda(resultado) if formatar else resultado

def diminuir(preco, taxa, formatar=False):
    resultado = preco * (1 - taxa / 100)
    return moeda(resultado) if formatar else resultado

def dobro(preco, formatar=False):
    resultado = preco * 2
    return moeda(resultado) if formatar else resultado

def metade(preco, formatar=False):
    resultado = preco / 2
    return moeda(resultado) if formatar else resultado

def moeda(preco):
    return f'R${preco:.2f}'.replace('.', ',')

preco = float(input("Digite o preço: "))

print(f"Preço original: {moeda(preco)}")
print(f"Preço com 10% de aumento: {aumentar(preco, 10, True)}")
print(f"Preço com 15% de desconto: {diminuir(preco, 15, True)}")
print(f"Dobro do preço: {dobro(preco, True)}")
print(f"Metade do preço: {metade(preco, True)}")
