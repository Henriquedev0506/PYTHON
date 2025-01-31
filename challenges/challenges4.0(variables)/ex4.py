distancia = float(input('qual a distancia da sua viagem? '))
print('voce esta prestes a começar uma viagem de {}km'.format(distancia))


'''if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45'''


preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('e o preco da sua viagem será de R${:.2f}'.format(preco))

