#Joguinho de advinhação

from random import randint
from time import sleep
computador = randint(0, 5)
print('*' * 40)
print('Joguinho de advinhação')
print('*' * 40)
print('Estou pensando em um número de 0 a 5,tente advinhar...')
jogador = int(input('Digite o número que você vai arriscar: '))
print('*' * 40)
print('processando...')
sleep(3)
if(jogador == computador):
    print('PARABÉNS!!! VOCÊ ACERTOU...')
else:
    print('VOCÊ PERDEU...')
    print(f'Eu pensei no número {computador}...')
    print(f'E não no número {jogador}...')
print('*' * 40)
