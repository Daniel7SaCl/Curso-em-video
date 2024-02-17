import random
a = str(input('Primeiro aluno:'))
b = str(input('Segundo aluno:'))
c = str(input('Terceiro aluno:'))
lista = [a,b,c]
random.shuffle(lista)
print('A ordem será: ')
print(lista)