time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    tot = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols o jogador {jogador["nome"]} fez na partida {c + 1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = str(input(f'Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('ERRO: Digite apenas S ou N...')
    if resposta in 'N':
        break

print('*' * 35)
print('cod.')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('*' * 35)
for k, v in enumerate(time):
    print(f'{k + 1} ', end='')
    for d in v.values():
        print(f'{str(d):<13} ', end='')
    print()
print('*' * 35)
