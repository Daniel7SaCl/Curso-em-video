d = float(input('Qual é a distancia da sua viajem?'))
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
print('E o preço da sua passagem sera de R${}'.format(p))