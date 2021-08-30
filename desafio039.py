from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de seu nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}...')
if idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o seu alistamento...')
elif idade == 18:
    print(f'Você possue 18 anos,deve se alistar o quanto antes...')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos...')
