from time import sleep
n = int(input('Digite u número para calcular o seu fatorial: '))
c = n
f = 1

print(f'Calculando o fatorial de {n} :')
print('Processando...')
sleep(5)
while c > 0:
    print(f'{c} x ')
    sleep(2)
    f *= c
    c -= 1

print(f'O fatorial de {n} é : {f}')
