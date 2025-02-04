print('{:=^40}'.format('LOJAS HENRIQUE'))
preco = float(input('preco das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista no cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao''')
opcao = int(input('Qual é a opcao? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('quantas parcelas?'))
    parcela = total / totparc
    print('sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela ))
print('sua compra de R${:.2f} vai custar R${:.2f} no final '.format(preco, total))

