from random import randint
from time import sleep
itens = ('Pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas Opcoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('qual a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('-=' * 11)
print('computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #PEDRA
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('JOGADOR GANHOU!')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')
elif computador == 1: #PAPEL
    if jogador == 0:
        print('COMPUTADOR GANHOU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHOU!')
elif computador == 2: #TESOURA
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU!')
    elif jogador == 2:
        print('EMPATE')
