lista = [[], []]
valor = 0
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(lista)
lista[0].sort()
print(f'Os números pares digitados e ordenados na crescente foram: {lista[0]}')
lista[1].sort()
print(f'Os números impares digitados e ordenados na crescente,foram: {lista[1]}')
