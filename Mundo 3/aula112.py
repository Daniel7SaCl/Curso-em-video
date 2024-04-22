def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print("Erro: por favor, digite um número inteiro válido.")
        else:
            return num

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except ValueError:
            print("Erro: por favor, digite um número real válido.")
        else:
            return num

numero_inteiro = leiaInt("Digite um número inteiro: ")
numero_float = leiaFloat("Digite um número real: ")
print("Número inteiro digitado:", numero_inteiro)
print("Número real digitado:", numero_float)
