from random import randint
from time import sleep
lista = []
jogos = []


print('*' * 35)
print('         PALPITES DA MEGASENA         ')
print('*' * 35)
quantidade = int(input('Quantos jogos você deseja gerar? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'**********SORTEANDO {quantidade} JOGOS**********')
sleep(5)
for i, l in enumerate(jogos):
    sleep(3)
    print(f'Jogo {i + 1} {l}')
print('-=' * 4, '< BOA SORTE! >','-=' * 4)
