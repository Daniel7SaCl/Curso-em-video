def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro: Digite um valor inteiro válido.")

# Exemplo de uso:
n = leiaInt('Digite um número inteiro: ')
print("Você digitou:", n)
