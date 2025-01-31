print('-' * 10, 'ANALISADOR DE TRIANGULOS','-' * 10)
l1 = float(input('digite o valor do primeiro lado: '))
l2 = float(input('digite o valor do segundo lado: '))
l3 = float(input('digite o valor do terceiro lado: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('ESSES LADOS PODEM FORMAR UM TRIANGULO!')
else:
    print('ESSES LADOS NAO PODEM FORMAR UM TRIANGULO!')