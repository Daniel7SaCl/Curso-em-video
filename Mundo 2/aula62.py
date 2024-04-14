N = int(input("Digite um número inteiro N: "))

f = [0, 1]

for i in range(2, N):
    proximo_termo = f[i - 1] + f[i - 2]
    f.append(proximo_termo)

print("Os", N, "primeiros elementos da Sequência de Fibonacci são:")
for termo in f[:N]:
    print(termo, end=" ")
