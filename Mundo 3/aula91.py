from datetime import datetime
ano_atual = datetime.now().year

funcionario = {}

funcionario['nome'] = input("Digite o nome do funcionário: ")
ano_nascimento = int(input("Digite o ano de nascimento do funcionário: "))
funcionario['idade'] = ano_atual - ano_nascimento
funcionario['carteira_de_trabalho'] = int(input("Digite o número da carteira de trabalho (0 se não tiver): "))

if funcionario['carteira_de_trabalho'] != 0:
    funcionario['ano_contratacao'] = int(input("Digite o ano de contratação: "))
    funcionario['salario'] = float(input("Digite o salário: "))
    anos_contribuicao = funcionario['ano_contratacao'] + 35 - ano_atual
    funcionario['aposentadoria'] = funcionario['idade'] + anos_contribuicao

print("\nDados do funcionário:")
for chave, valor in funcionario.items():
    print(f"{chave.capitalize()}: {valor}")
