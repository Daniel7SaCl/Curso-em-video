n = (int(input('Fale um numero: ')))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('A unidade,dezena,centena e milhar do seu numero sao respectivamente {},{},{},{}'.format(n,d,c,m))
