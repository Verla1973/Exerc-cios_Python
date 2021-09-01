soma = quantidade = media = 0
resposta = 'S'
maior = 0
menor = 0

while resposta in 'Ss':

    num = int(input('Digite um número: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    media = soma / quantidade
    resposta = str(input('Você quer continuar[S/N]? ')).strip().upper()[0]

print(f'Você digitou {quantidade} números...')
print(f'A soma deles foi: {soma}...')
print(f'A média de todos os números somados foi {media:.2f}')
print(f'O menor número digitado foi {menor}...')
print(f'O maior número digitado foi {maior}...')
print('===ACABOU---')
