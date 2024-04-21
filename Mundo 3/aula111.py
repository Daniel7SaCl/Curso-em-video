def leiaDinheiro(mensagem):
    while True:
        valor = input(mensagem).replace(',', '.')
        if valor.replace('.', '').isdigit():
            return float(valor)
        else:
            print('Valor inválido. Digite um valor monetário válido.')

preco = leiaDinheiro("Digite o preço: R$")
print(f"Você digitou: R${preco:.2f}")
