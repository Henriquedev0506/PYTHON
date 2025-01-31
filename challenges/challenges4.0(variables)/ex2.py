km = int(input('qual a velocidade do carro?'))
valor = 150 + ((km - 80) * 7)
if km > 80:
    print('voce foi MULTADO por ultrapassar a velocidade maxima de 80km/h')
    print('valor da multa: R${}'.format(valor))
else:
    print('tenha um bom dia! dirija com segurança')


