tabela = ('Internacional', 'Bahia', 'Cruzeiro', 'Chapecoense', 'São Paulo', 'Atlético',
          'Flamengo', 'Fluminense', 'Grêmio', 'Coritiba', 'Atlético/PR', 'Santos', 'Palmeiras',
          'Corinthians', 'Bragantino', 'Vasco', 'Botafogo', 'Atlético/GO',
          'Sport', 'Vitória')

print('-=' * 25)
print('**********TABELA DO BRASILEIRÃO 2021**********')
print(tabela)
print('-=' * 25)
print('Os cinco primeiros colocados no Brasileirão:')
print(f'{tabela[:5]}')
print('-=' * 25)
print('Os 4 últimos colocados e na zona de rebaixamento são:')
print(f'{tabela[-4:]}')
print('-=' * 25)
print(f'A Chapecoense está na ',tabela.index('Chapecoense') + 1,'ª posição')
print('-=' * 25)
print('**********TABELA EM ORDEM ALFABÉTICA**********')
print(sorted(tabela))
print('-=' * 25)
