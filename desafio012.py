preco = float(input('Digite o preço do produto: '))
desconto = (preco * 0.05)
preco_novo = (preco - desconto)

print(f'Olá, seu produto custava R$ {preco}...')
print(f'Com o desconto,ficou custando R$ {preco_novo}...')
