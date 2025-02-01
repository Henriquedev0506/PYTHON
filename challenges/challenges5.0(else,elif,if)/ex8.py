peso = float(input('qual e seu peso? (Kg) '))
altura = float (input('qual a sua altura? (m) '))
imc = peso / (altura ** 2)
print('o IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('voce está abaixo do PESO normal')
elif 18.5 <= imc <= 25:
    print('parabens! voce esta na faixa de peso normal')
elif 25 <= imc <= 30:
    print('voce esta em SOBREPESO')
elif 30 <= imc <40:
    print('voce está em obesidade, cuidado')
elif imc >= 40:
    print('voce está em obesidade MORBIDA, cuidado')