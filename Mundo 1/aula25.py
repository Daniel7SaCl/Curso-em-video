f = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(f.count('A')))
print('A primeira letra A apareceu na posiçao {}'.format(f.find('A')+1))
print('A ultima letra A aparece na posiçao {}'.format(f.find('A')+1))