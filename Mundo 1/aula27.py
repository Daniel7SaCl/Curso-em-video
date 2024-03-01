from random import randint
com = randint(0,5)
print('Pensando em um numero de 0 a 5...')
J = int(input('Em que numero eu pensei? '))
if J == com:
    print('Parabens voce venceu!!')
else:
    print('Perdeu, pensei em {}'.format(com))