n = int(input('Digite um numero inteiro:'))
print('''Escolha bases para a conversao:
[ 1 ] converter para binario
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
o = int(input('Sua opcao sera: '))
if o == 1:
    print('{} convertido para binario é igual a {}'.format(n,bin(n)))
elif o == 2:
    print('{} convertido para octal é igual a {}'.format(n,oct(n)))
elif o == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(n,hex(n)))
else:
    print('Opcao invalida')    

