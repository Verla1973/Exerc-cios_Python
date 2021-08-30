preco_atual = float(input('Digite o valor do produto: R$ '))

preco_a_vista = preco_atual - (preco_atual * 0.10)
preco_a_vista_cartao = preco_atual - (preco_atual * 0.05)
prazo = preco_atual + (preco_atual * 0.20)

print('*' * 40)
print(f'O preço do produto é R$ {preco_atual}')
print(f'Á vista/cheque com 10% de desconto ele fica R$ {preco_a_vista}...')
print('*' * 40)
print(f'O preço á vista com cartão,com 5% de desconto,fica R$ {preco_a_vista_cartao}...')
print(f'O preço do produto em até 2X no cartão fica em duas vezes de R$ {preco_atual / 2}')
print(f'O produto em 3x fica: 3 x de R$ {prazo / 3}')
print(f'O produto em 4x fica: 4 x de R$ {prazo / 4}')
