n = int(input('Digite um valor e eu lhe direi sua tabuada: '))
for c in range(1,11):
    print('{} * {:2} = {}'.format(n, c, (n * c)))
print('FIM DA TABUADA DO {}'.format(n))