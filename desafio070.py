gastoTotal = maisBarato = maisMil = cont = 0
nomeBarato = ' '

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto:R$ '))
    cont += 1
    gastoTotal += preco
    if cont == 1:
        maisBarato = preco
        nomeBarato = produto
    else:
        if preco < maisBarato:
            maisBarato = preco
            nomeBarato = produto
    if preco >= 1000:
        maisMil += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? (S/N): ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'A soma total dos produtos foi R$ {gastoTotal}')
print(f'Ao todo tivemos {maisMil} produtos com preços acima de mil reais...')
print(f'O produto mais barato registrado foi {nomeBarato} a R$ {maisBarato}')
print('**********FIM**********')
