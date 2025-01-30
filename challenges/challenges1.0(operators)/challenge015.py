km = float(input('quantos kilometros voce percorreu com o nosso carro? KM'))
dias = int(input('quantos dias o carro foi usado? '))
pago =(km * 0.15) + (dias * 60)
print('-' * 8, 'ALUGUEL DE CARROS','-' * 8)
print('O total a pagar é de R${:.2f}'.format(pago))







