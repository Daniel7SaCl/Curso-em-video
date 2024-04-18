palavras = ("python", "programacao", "computador", "linguagem", "inteligencia", "artificial")

for palavra in palavras:
    vogais_palavra = [letra for letra in palavra if letra in "aeiou"]
    print(f"Vogais em '{palavra}':", vogais_palavra)