from datetime import date
a = date.today().year
n = int(input('Ano de nascimento: '))
i = a - n
if i >= 18:
    print('Alistamento obrigatorio')
elif i < 18:
    d = 18 - i
    print('Ainda falta {}ano/s para voce se alistar'.format(d))
