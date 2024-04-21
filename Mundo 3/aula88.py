num_alunos = int(input("Quantos alunos serão cadastrados? "))

alunos = []
for i in range(1, num_alunos + 1):
    nome = input(f"Digite o nome do {i}º aluno: ")
    nota1 = float(input(f"Digite a primeira nota do(a) aluno(a) {nome}: "))
    nota2 = float(input(f"Digite a segunda nota do(a) aluno(a) {nome}: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])

print("\nBoletim:")
for aluno in alunos:
    nome = aluno[0]
    media = aluno[2]
    print(f"Aluno: {nome} - Média: {media:.2f}")

mostrar_notas = input("\nDeseja ver as notas de algum aluno individualmente? (S/N): ")
if mostrar_notas.upper() == 'S':
    aluno_escolhido = input("Digite o nome do aluno que deseja ver as notas: ")
    encontrado = False
    for aluno in alunos:
        if aluno[0] == aluno_escolhido:
            print(f"Notas de {aluno_escolhido}: {aluno[1]}")
            encontrado = True
            break
    if not encontrado:
        print("Aluno não encontrado.")
