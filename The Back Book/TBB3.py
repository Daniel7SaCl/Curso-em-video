import json
from datetime import datetime

print('SEJA BEM VINDO AO THE BACK BOOK')

def carregar_dados():
    try:
        with open('biblioteca.json', 'r') as file:
            dados = json.load(file)
            return dados['livros'], dados['emprestimos']
    except FileNotFoundError:
        return {}, {}

def salvar_dados():
    with open('biblioteca.json', 'w') as file:
        dados = {'livros': livros, 'emprestimos': emprestimos}
        json.dump(dados, file, indent=4)

livros, emprestimos = carregar_dados()

def adclivros():
    nomedolivro = input('Qual livro deseja armazenar? ')
    autor = input('Quem é o autor do livro? ')
    livros[nomedolivro] = autor
    salvar_dados()
    print(f"Livro '{nomedolivro}' de {autor} adicionado com sucesso!")

def mostlivros():
    if not livros:
        print('Nao ha livros!')
    else:
        print('Livros:')
        for nomedolivro, autor in livros.items():
            print(f'{nomedolivro} de {autor}')

def empreslivro():
    nomedolivro = input('Qual livro deseja emprestar? ')
    if nomedolivro in emprestimos and not emprestimos[nomedolivro]['devolvido']:
        print(f"O livro '{nomedolivro}' já está emprestado.")
    elif nomedolivro in livros:
        importancia = input('Qual a importância do livro? ')
        data_emprestimo = datetime.now().strftime('%Y-%m-%d')
        emprestimos[nomedolivro] = {
            'importancia': importancia,
            'data_emprestimo': data_emprestimo,
            'devolvido': False
        }
        salvar_dados()
        print(f"Livro '{nomedolivro}' emprestado com sucesso!")
    else:
        print(f"O livro '{nomedolivro}' não está disponível na biblioteca.")

def devollivro():
    nomedolivro = input('Qual livro deseja devolver? ')
    if nomedolivro in emprestimos and not emprestimos[nomedolivro]['devolvido']:
        emprestimos[nomedolivro]['devolvido'] = True
        salvar_dados()
        print(f"Livro '{nomedolivro}' devolvido com sucesso!")
    else:
        print(f"O livro '{nomedolivro}' não está registrado como emprestado.")

def listaremprestimos():
    if not emprestimos:
        print('Nao ha empréstimos!')
    else:
        print('Empréstimos:')
        for nomedolivro, detalhes in emprestimos.items():
            devolvido = "Sim" if detalhes['devolvido'] else "Não"
            print(f"Título: {nomedolivro}")
            print(f"  Importância: {detalhes['importancia']}")
            print(f"  Data de Empréstimo: {detalhes['data_emprestimo']}")
            print(f"  Devolvido: {devolvido}")
            print()

while True:
    print("\nMenu:")
    print('[1] Adicionar livro')
    print('[2] Mostrar livros armazenados')
    print('[3] Emprestar livro')
    print('[4] Devolver livro')
    print('[5] Listar empréstimos')
    print('[6] Sair')

    escolha = input('Escolha uma opção (1-6): ')
    
    if escolha.isdigit():
        escolha = int(escolha)
        if escolha == 1:
            adclivros()
        elif escolha == 2:
            mostlivros()
        elif escolha == 3:
            empreslivro()
        elif escolha == 4:
            devollivro()
        elif escolha == 5:
            listaremprestimos()
        elif escolha == 6:
            print('Obrigado, volte sempre!')
            break
        else:
            print('Escolha inválida!!!')
    else:
        print('Por favor, insira um número válido.')
