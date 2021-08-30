from datetime import date

nome_atleta = str(input('Digite o nome do atleta: '))
ano_nascimento = int(input('Digite o ano de nascimento do aluno: '))
idade_atleta = date.today().year - ano_nascimento

if idade_atleta <= 9:
    print(f'O atleta {nome_atleta} tem {idade_atleta} anos...')
    print(f'O atleta pertence a categoria Mirim...')
elif idade_atleta <= 14:
    print(f'O atleta {nome_atleta} tem {idade_atleta} anos...')
    print(f'O atleta pertence a categoria Infantil...')
elif idade_atleta < 19:
    print(f'O atleta {nome_atleta} tem {idade_atleta} anos...')
    print(f'O atleta pertence a categoria Junior...')
elif idade_atleta <= 20:
    print(f'O atleta {nome_atleta} tem {idade_atleta} anos...')
    print(f'O atleta pertence a categoria Sênior...')
else:
    print(f'O atleta {nome_atleta} tem {idade_atleta} anos...')
    print(f'O atleta pertence a categoria Master...')
