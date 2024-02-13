S = float(input('Qual é o salario do trabalhador? '))
A = float(input('Qual será o aumento? '))
S2 = S * (A/100)
print('O salario do tralhador com o aumento de {}%, será R${:.1f}'.format(A,S2))