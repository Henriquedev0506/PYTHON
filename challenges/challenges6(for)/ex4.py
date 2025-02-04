n = int(input('Digite um valor e eu lhe direi sua tabuada: '))
x = 0
for c in range(0,10):
    x = x + 1
    print('{} * {} = {}'.format(n, x, (n * x)))
print('FIM DA TABUADA DO {}'.format(n))