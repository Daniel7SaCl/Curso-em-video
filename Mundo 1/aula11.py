P = float(input('Preço do produto: R$'))
D = float(input('Qual será o desconto:'))
N = P * (D / 100)
print('Com o desconto de {}%, o preço do produto ficará R${:.1f}'.format(D,N))