nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
nota3 = float(input('Digite a terceira nota do aluno: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f'O aluno teve média {media}...')
    print('APROVADO...Parabéns!!!')
elif media >= 5:
    print(f'O aluno teve média {media}...')
    print('O aluno ficou em RECUPERAÇÃO...')
else:
    print(f'O aluno teve média {media}...')
    print('REPROVADO...')
