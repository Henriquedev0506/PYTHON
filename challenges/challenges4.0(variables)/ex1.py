from random import randint
from time import sleep
computador = randint(0,5)
print('-=-' * 20)
print('vou pensar em um numero entre 0 e 5. tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABENS!, voce conseguiu me vencer')
else:
    print('Ganhei, eu pensei no numero {} e nao no {}'.format(computador, jogador))