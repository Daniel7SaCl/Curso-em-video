p = int(input('primeiro termo: '))
r = int(input('razao: '))
t = int(input('numero de termos: '))
n = p + ( t -1) *r
for c in range(p, n + r, r):
    print('{}'.format(c), end= '-')
