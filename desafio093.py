jogador = {}
partidas = []
jogador['nome'] = str(input('Digite o nome do jogador: '))
tot = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols o jogador {jogador["nome"]} fez na partida {c + 1}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('*' * 30)
print(jogador)
print('*' * 30)
print(f'O jogador {jogador["nome"]} fez um total de {len(jogador["gols"])} partidas...')
for i, v in enumerate(jogador['gols']):
    print(f'O jogador {jogador["nome"]} na partida {i + 1} fez {v} gols...')
print('*' * 30)
print(f'Somando um total de {jogador["total"]} gols...')
print(f'*' * 10,'<FIM DA ANÁLISE>','*' * 10)
