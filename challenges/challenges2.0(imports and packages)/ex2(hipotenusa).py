from math import hypot
cA = float(input('digite o valor do cateto triangulo retangulo: '))
cO = float(input('digite o valor do outro cateto: '))
Hip = hypot(cA, cO)
print('o valor da hipotenusa é {:.2f}'. format(Hip))

