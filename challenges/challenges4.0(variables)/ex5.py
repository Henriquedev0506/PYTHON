from datetime import date
ano = int(input('que ano voce quer analisar? escreva 0 para analisar o ano atual '))
if ano == 0:
    ano = date.today().year
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('o ano {} é Bissexto'.format(ano))
else:
    print('ano {} Não é bissexto'.format(ano))