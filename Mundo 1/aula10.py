lar = float(input('Largura da parede:  '))
alt = float(input('Altura da parede:   '))
A = lar * alt
tin = A / 2
print('A área dessa parede é {}m2 e sua dimensão de {}x{}'.format(A,lar,alt))
print('Então para pintar será necessário {}L de tinta'.format(tin))