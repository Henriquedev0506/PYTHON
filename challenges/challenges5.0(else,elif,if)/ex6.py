from datetime import date
nasc = int(input('digite o ano de seu nascimento: '))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif  idade <= 25:
    print('Sua categoria é SÊNIOR')
elif nasc > 25:
    print('Sua categoria é MASTER')