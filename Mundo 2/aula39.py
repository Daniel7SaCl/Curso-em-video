n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
m = (n1 + n2 + n3) / 3
if 7 > m >= 5:
    print('Voce esta em reculperaçao')
elif m >= 7:
    print('Voce esta aprovado')
else:
    print('Voce nao foi aprovado')