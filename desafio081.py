valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? ')).strip()[0]
    if resposta in 'Nn':
        break
print('*' * 30)
print(f'O total de números digitados foram {len(valores)}...')
valores.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente foram: ')
print(valores)
if 5 in valores:
    print(f'O valor 5 faz parte da lista...')
else:
    print(f'O valor 5 não foi encontrado na lista...')
