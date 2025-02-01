from datetime import date
atual = date.today().year
nasc = int(input('ano de nascimento: '))
idade = atual - nasc
print('quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('voce tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('voce ainda nao tem 18 anos, ainda falta {} anos para o alistamento'.format(saldo))

elif idade > 18:
    saldo = idade - 18
    print('voce ja deveria ter se alistado ha {} anos'.format(saldo))











