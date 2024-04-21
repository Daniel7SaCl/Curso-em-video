def fatorial(numero, show=False):
    resultado = 1
    processo = ''
    
    if show:
        processo += f'{numero}! = '

    for i in range(1, numero + 1):
        resultado *= i
        if show:
            if i != 1:
                processo += ' × '
            processo += str(i)

    if show:
        processo += f' = {resultado}'
        print(processo)
    return resultado

num = int(input("Digite um número para calcular o fatorial: "))
mostrar_processo = input("Deseja mostrar o processo de cálculo? (S/N): ").upper()

if mostrar_processo == 'S':
    fatorial(num, show=True)
else:
    print("Resultado:", fatorial(num))