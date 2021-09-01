#script que analisa a idade de um grupo de pessoas

mediaidade = 0
somaidade = 0
maioridadehomem = 0
nomevelho = ''
mulhermenor = 0

for p in range(1, 5):
    print(f'------{p}ª PESSOA------')
    nome = str(input(f'Nome: '))
    idade = int(input(f'Idade: '))
    sexo = str(input('Sexo [M/F]:' )).strip()
    somaidade += idade
    if sexo in 'Ff' and idade < 21:
        mulhermenor += 1
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    mediaidade = somaidade / p

print(f'A média de idade do grupo é de {mediaidade:.2f} anos...')
print(f'O homm mais velho do grupo se chama: {nomevelho.upper()} e possue {maioridadehomem} anos...')
print(f'No grupo também estão {mulhermenor} pessoas do sexo feminino menores de idade...')
