from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 10 valores da lista...', end='')
    sleep(5)
    for cont in range(0, 10):
        n = randint(1, 50)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(4)
    print('PRONTO!!!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares de {lista} é {soma}...')


numeros = []
sorteia(numeros)
somapar(numeros)
