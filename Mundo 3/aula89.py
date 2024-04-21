num_alunos = int(input("Quantos alunos serão cadastrados? "))

alunos = {}
for i in range(1, num_alunos + 1):
    nome = input(f"Digite o nome do {i}º aluno: ")
    media = float(input(f"Digite a média do(a) aluno(a) {nome}: "))
    situacao = "Aprovado" if media >= 7 else "Reprovado"
    alunos[nome] = {'Média': media, 'Situação': situacao}

print("\nDados dos alunos:")
for nome, dados in alunos.items():
    print(f"Aluno: {nome} - Média: {dados['Média']:.2f} - Situação: {dados['Situação']}")
