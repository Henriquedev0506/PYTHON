n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))
maior = n1
if n2 > n1:
    maior = n2
    print('o maior numero é {}'.format(n2))
elif n1 == n2 :
    print('os valores {} e {} sao iguais'.format(n1, n2))
else:
    print('o maior valor é {}'.format(n1))




