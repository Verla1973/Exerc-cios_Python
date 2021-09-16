galera = []
pessoa = {}
soma = 0
maior_media = 0
maior = ''

while True:
    pessoa['nome'] = str(input('Digite o nome da pessoa: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO: Você deve digitar M ou F...')
    pessoa['idade'] = int(input('Idade: '))

    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('ERRO: Você deve digitar S ou N')
    if resposta == 'N':
        break
print('-=' * 30)
print(f'Ao todo foram cadastradas {len(galera)} pessoas...')
media = soma / len(galera)
print(f'A média de idade das pessoas cadastradas {media:.2f} anos...')
print(f'As mulheres cadastradas foram: ',end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}...', end='')
print()
print(f'As pessoas com idade acima da média são: ', end='')
for i in galera:
    if i['idade'] > media:
        print(f' {i["nome"]}...', end='')
