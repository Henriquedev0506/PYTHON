r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um TRIANGULO', end=" ")
    if r1 == r2 and r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 !=r1:
        print('ESCALENO!')
    else:
        print('ISOSCELES')

else:
    print('os segmentos acima NAO PODEM FORMAR triangulo')