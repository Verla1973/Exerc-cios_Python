from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 13)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 13)
if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE...')
    elif jogador == 1:
        print('Jogador vence...')
    elif jogador == 2:
        print('Computador vence...')
    else:
        print('Jogada inválida...')

if computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('Computador vence...')
    elif jogador == 1:
        print('Empate...')
    elif jogador == 2:
        print('Jogador vence...')
    else:
        print('Jogada inválida...')

if computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print('Jogador vence...')
    elif jogador == 1:
        print('Computador vence...')
    elif jogador == 2:
        print('Empate...')
    else:
        print('Jogada inválida...')
