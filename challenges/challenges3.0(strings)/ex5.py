frase = str(input('digite uma frase: ')).upper().strip()
print('a letra A aparece {} vezes'.format(frase.count('A')))
print('a primeira letra A aparece na posicao {}'.format(frase.find('A')+1))
print('a ultima letra A apareceu na posicao {}'.format((frase.rfind('A')+1)))