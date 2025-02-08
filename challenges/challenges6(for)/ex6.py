ate = int(input('ate qual posicao voce quer a progressao?: '))
primeiro = int(input('Primeiro termo: '))
razao = int(input('RAZAO: '))
prog = primeiro + (ate) * razao
for c in range (primeiro, prog, razao):
    print('{}'.format(c), end = ' - ')
print('ACABOU')