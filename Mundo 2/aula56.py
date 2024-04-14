s = str(input('qual o seu sexo? M/F')).upper
while s not in 'MmFf':
    s = str(input('sexo invalido, informe novamente'))
print('sexo registrado')
