expressao = input("Digite uma expressão com parênteses: ")

pilha = []
for char in expressao:
    if char == '(':
        pilha.append(char)
    elif char == ')':
        if not pilha:
            print("Os parênteses estão desbalanceados.")
            break
        pilha.pop()  
else:
    if not pilha:
        print("Os parênteses estão balanceados.")
    else:
        print("Os parênteses estão desbalanceados.")
