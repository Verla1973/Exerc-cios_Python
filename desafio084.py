temp = []
princ = []
maior = menor = 0


while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? ')).strip()[0]
    if resp in 'Nn':
        break
print('*' * 30)
print(f'Os dados cadastrados foram:')
print(princ)
print(f'Ao total foram cadastradas {len(princ)}...')

print(f'O maior peso registrado foi {maior} kgs de: ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}...', end='')
print()
print(f'O menor peso registrado foi {menor} kgs de: ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}...', end='')
