p = float(input('Quando voce pesa?'))
a = float(input('Qual sua altura?'))
imc = p / (a**2)
if imc < 18.5:
    print('Abaixo do peso comum')
elif 18.5<= imc <= 25:
    print('Peso comum')
elif 25 <= imc < 30:
    print('Acima do peso comum')
else:
    print('Obesidade')
