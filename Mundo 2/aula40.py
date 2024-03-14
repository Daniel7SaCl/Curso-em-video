from datetime import date
a=date.today().year
n = int(input('Que dia voce nasceu?'))
i =  a - n
print('Voce pertence a classificaçao:')
if i <= 9:
    print('MIRIM')
elif i <= 14:
    print('INFANTIL')
elif i <= 19:
    print('JUNIOR')
else:
    print('SENIOR')