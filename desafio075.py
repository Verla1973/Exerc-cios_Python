numeros = (int(input('Digite o primeiro valor: ')),
           int(input('Digite o segundo valor: ')),
           int(input('Digite o terceiro valor: ')),
           int(input('Digite o quarto valor: ')))
print(f'Você digitou os números {numeros}')
print(f'O valor 9 foi digitado {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O número 3 apareceu pela primeira vez na {numeros.index(3) + 1}ª posição.')
else:
    print('O numero 3 não foi digitado')
print(f'Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'{n}-', end='')
