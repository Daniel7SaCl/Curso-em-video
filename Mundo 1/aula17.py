import math
a = float(input('Digite o angulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O seno desse angulo equivale a {} o cosseno {} e a tangente{}'.format(s,c,t))
