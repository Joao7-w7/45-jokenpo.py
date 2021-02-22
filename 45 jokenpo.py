from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções:
\033[4;32m[0] PEDRA \033[m
\033[4;33m[1] PAPEL \033[m
\033[4;34m[2] TESOURA \033[m''')
jogador = int(input('Qual e a sua jogada? '))
print('\033[4;35mJO\033[m')
sleep(1)
print('\033[4;36mKEN\033[m')
sleep(1)
print('\033[4;33mPO\033[m!!!')
print('-=-'*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=-'*11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA! ')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADAR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENSE')
    else:
        print('JOGADA INVALIDA! ')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA! ')