s=0
c=0
for c in range(1,7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        s += n 
        c += 1
    print('Voce informou {} numeros pares e a soma foi {}'.format(c,s))