
nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
print(f'Seu nome em letras maiúsculas fica assim: {nome.upper()}...')
print(f'Seu nome em letras minúsculas fica assim: {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - (nome.count(" "))} letras...')
print(f'Seu primeiro nome tem {nome.find(" ")} letras...')
