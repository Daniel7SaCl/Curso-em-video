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

def resumo(preco, aumento, desconto):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{desconto}% de desconto: \t{diminuir(preco, desconto, True)}')
    print('-' * 30)

