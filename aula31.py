ano = int(input('Diga me um ano:'))
if ano % 4 == 0 and ano % 100 == 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} nao é bissexto'.format(ano))

