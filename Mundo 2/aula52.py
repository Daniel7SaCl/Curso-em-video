f = str(input('Digite uma frase: ')).split()
p = f.split()
j = ''.join(p)
i =  ''
for l in range(len(j) - 1, -1, -1):
    i+= j[l]
if i == j:
    print('temos um palindromo!')
else:
    print('A frase nao é um palindromo!')