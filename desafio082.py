lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? ')).strip()[0]
    if resposta in 'Nn':
        break
for p in lista:
    if p % 2 == 0:
        par.append(p)

    else:
        if p % 2 == 1:
            impar.append(p)


print(f'Os valores digitados foram:')
print(lista)
print(f'Os valores par digitados foram: ')
print(par)
print('Os valores impar digitados foram: ')
print(impar)
