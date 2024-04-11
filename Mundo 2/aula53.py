from datetime import datetime

pessoas = 7
atingiram_maioridade = sum(1 for _ in range(pessoas) if (idade := datetime.now().year - datetime.strptime(input("Informe a data de nascimento (dd/mm/aaaa): "), "%d/%m/%Y").year) >= 18)
ja_morreram = sum(1 for _ in range(pessoas) if (idade := datetime.now().year - datetime.strptime(input("Informe a data de nascimento (dd/mm/aaaa): "), "%d/%m/%Y").year) < 0)

print(f"\nQuantidade de pessoas que atingiram a maioria: {atingiram_maioridade}")
print(f"Quantidade de pessoas que já morreram: {ja_morreram}")
