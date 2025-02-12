from datetime import date
totmaior = 0
totmenor = 0
atual = date.today().year
for pess in range(1,8):
    nasc = int(input('Em que ano a {}a pessoa nasceu?'.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
       totmenor += 1
print('ao todo tiveram {} maiores '.format(totmaior))
print('ao todo tiveram {} menores'.format(totmenor))



