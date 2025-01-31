valCasa = float(input('qual o valor da casa R$'))
valS = float(input('qual o seu salário? R$'))
anos = int(input('quantos anos voce vai pagar? '))
meses = anos * 12
parcelas = valCasa / meses
if parcelas > (valS * 30/100):
    print('voce nao pode comprar essa casa com o seu salario')
else:
    print('a prestaçao a pagar, por mes, vai ser de R${:.2f} por {} meses ou {} anos'.format(parcelas, meses, anos))