a = int(input('Primeiro valor:'))
b = int(input('Segungo valor:'))
c = int(input('Terceiro valor:'))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
  maior = b
if c>a and c>b:
    maior = c
print('O maior valor foi {} e o menor {}'.format(maior,menor))