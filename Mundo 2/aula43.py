p = float(input('Qual o preço do produto?'))
o = int(input(((('''
1 - dinheiro
2 - a vista
3 - 2x no cartao
4 - 3x cartao
Forma de pagamento: ''')))))
if o == 1:
    t = (p * 10/100)
elif o == 2:
    t = (p * 5/100)
elif o == 3:
    t = p
    par = t / 2
elif o == 4:
    t = p + (p * 20/100)
    tpar = int(input('Quantas parcelas?'))
    par = t / tpar
    print('Sua compra tera parcela de {}x de R${} com juros'.format(tpar,par ))
else:
    t = 0
    print('Opcao invalida')
print('Sua conta de R${:.2f} vai custar R${:.2f}'.format(p, t))