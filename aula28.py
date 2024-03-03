v = float(input('Qual a velocidade do carro?'))
if v>80:
    print('MULTADO!!! Voce exedeu o limite de 80km/h')
    m = (v-80)*7
    print('Voce pagara a multa de R${:.2f}'.format(m))
else:
    print('Tenha um bom dia e dirija com cuidado!')