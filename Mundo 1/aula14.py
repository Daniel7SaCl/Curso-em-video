d = int(input('Quantos dias alugados?'))
k = float(input('Quantos Km rodados?'))
P = (d * 60) + (k * 0.15)
print('O total a ser pago será R${:.2f}'.format(P))