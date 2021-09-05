# tabela de preços formatada
listagem = ('Lápis', 1.75,
            'Caneta', 2.25,
            'Caderno', 16.50,
            'Mochila', 130,
            'Livro', 65)
print('*' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('*' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')
print('*' * 40)
