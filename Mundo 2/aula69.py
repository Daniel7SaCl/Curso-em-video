total_gasto = 0
produtos_mais_de_1000 = 0
nome_produto_mais_barato = ''
preco_produto_mais_barato = float('inf')  

while True:
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: R$"))

    total_gasto += preco_produto

    if preco_produto > 1000:
        produtos_mais_de_1000 += 1

    if preco_produto < preco_produto_mais_barato:
        nome_produto_mais_barato = nome_produto
        preco_produto_mais_barato = preco_produto
    
    continuar = input("Deseja cadastrar mais um produto? (S para Sim, N para Não): ").upper()
    if continuar != 'S':
        break

print("A) Total gasto na compra: R$", total_gasto)
print("B) Quantidade de produtos que custam mais de R$1000:", produtos_mais_de_1000)
print("C) Nome do produto mais barato:", nome_produto_mais_barato)
