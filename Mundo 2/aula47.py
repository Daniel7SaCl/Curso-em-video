s = 0
c = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + 1
        c = c + 1
print('A soma dos {} valores solicitados é {}'.format(c,s))
