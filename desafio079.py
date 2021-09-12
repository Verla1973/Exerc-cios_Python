numeros = []

while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print(f'Numero {n} adicionado com sucesso!')
    else:
        print(f'Número {n} duplicado,não vou adicionar...')

    r = str(input('Quer continuar? ')).strip()[0]
    if r in 'Nn':
        break

print('*' * 30)
numeros.sort()
print(f'Você digitou os seguintes números:')
print(numeros)
