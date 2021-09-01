registro = ''
sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Opção inválida,digite o sexo novamente: ')).strip().upper()[0]
    if sexo == 'M':
        registro = 'MASCULINO'
    if sexo == 'F':
        registro = 'FEMININO'
print(f'Sexo {registro} registrado com sucesso...')
