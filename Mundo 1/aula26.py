n = str(input('Digite seu nome: ')).strip()
no = n.split()
print('Seu primeiro nome é {}'.format(no[0]))
print('Seu ultimo nome é {}'.format(no[len(no)-1]))