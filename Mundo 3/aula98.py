def maior(*numeros):
    if len(numeros) == 0:
        print("Nenhum número fornecido.")
    else:
        maximo = numeros[0]
        for num in numeros:
            if num > maximo:
                maximo = num
        print(f"O maior número é: {maximo}")

maior(10, 5, 8, 20, 15)
