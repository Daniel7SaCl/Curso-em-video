print('SEJA BEM VINDO AO THE BACK BOOK')

livro = {}
def adclivros():
    nomedolivro = input('Qual livro deseja armazenar? ')
    autor = input('Quem é o autor do livro?')
    livro[nomedolivro] = autor
def mostrar():
    if not livro:
        print('Nao ha livros!')
    else:
        print('Livros:')
        for nomedolivro, autor in livro.items():
            print(f'{nomedolivro} de {autor}')

while True:
    print("\nMenu:")
    print('[1] Adicionar o livro')
    print('[2] Mostrar livros armazenados')
    print('[3] Sair')

    escolha = int(input('Escolha uma opcao(1,2 ou 3):'))

    if escolha == 1:
        adclivros()
    elif escolha == 2:
        mostrar()
    elif escolha == 3:
        print('Obrigado, volte sempre!')
        break
    else:
        print('Escolha invalida!!!')
