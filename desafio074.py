from random import randint
numeros = (randint(0, 100), randint(0, 100), randint(0, 100),
           randint(0, 100), randint(0, 100))
print('Os números sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print('-='* 10)
print(f'O maior número sorteado foi {max(numeros)}...')
print(f'O menor número sorteado foi {min(numeros)}...')
