r1=int(input('Primeiro segmento: '))
r2=int(input('Segundo segmento: '))
r3=int(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3:
    print('Os segmentos PODEM formar um triangulo!')
else:
    print('Os segmentos NAO PODEM formar um triangulo!')