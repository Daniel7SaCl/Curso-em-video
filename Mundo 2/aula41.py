r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Esses segmentos podem fomam um triangulo.")
    if r1 == r2 == r3:
        print('EQUILATERO')
    if r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Esses segmentos nao formam um triagulo')

    
