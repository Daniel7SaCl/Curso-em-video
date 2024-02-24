from random import choice
a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno:  '))
c = str(input('Terceiro aluno:  '))
l = (a,b,c)
E = choice(l)
print('O aluno escolhido foi {}'.format(E))
