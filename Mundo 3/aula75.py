produtos_precos = (
    ("Lápis", 1.50),
    ("Caneta", 2.00),
    ("Caderno", 15.90),
    ("Borracha", 1.00),
    ("Régua", 3.50)
)

print("Listagem de Preços:")
print("-" * 30)
print("{:<10} {:<10}".format("Produto", "Preço"))
print("-" * 30)
for produto, preco in produtos_precos:
    print("{:<10} R${:<10.2f}".format(produto, preco))
print("-" * 30)