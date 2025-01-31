salario = float(input('qual o salario do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:novo = salario + (salario * 10 / 100)
print('quem ganhava R${:.2f} pasa a ganhar R${:.2f} agora.'.format(salario, novo))