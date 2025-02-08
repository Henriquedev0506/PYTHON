num = int(input('Digite um numero: '))
Tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        Tot += 1
    else:
        print('\033[32m', end='')
    print('{} '.format(c), end = ' ')
print('\n\033[mo numero {} foi dividido {} vezes'.format(num,Tot))
if Tot == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele nao é primo   59                          Q8  777 777')