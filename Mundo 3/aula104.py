def notas(*notas, situacao=False):
    quantidade = len(notas)
    maior_nota = max(notas)
    menor_nota = min(notas)
    media = sum(notas) / quantidade

    info = {
        "Quantidade de notas": quantidade,
        "Maior nota": maior_nota,
        "Menor nota": menor_nota,
        "Média da turma": media
    }

    if situacao:
        if media >= 7:
            info["Situação"] = "Aprovado"
        elif 5 <= media < 7:
            info["Situação"] = "Recuperação"
        else:
            info["Situação"] = "Reprovado"

    return info

notas_alunos = (7.5, 8.0, 6.5, 9.0, 5.0)
info_notas = notas(*notas_alunos, situacao=True)

for chave, valor in info_notas.items():
    print(f"{chave}: {valor}")
