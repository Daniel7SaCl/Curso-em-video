c = float(input('Valor da casa:'))
s = float(input('Salario do comprador:'))
a = int(input('Quantos anos de financiamento? '))
p = c / (a * 12)
m = s * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(c,a))
print('A prestaçao sera de {:.2f}'.format(p))
if p <= m:
    print('O emprestimo podera ser concedido')
else:
    print('Emprestimo negado')