ficha = []


while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar [S/N]? ')).strip()[0]
    if resposta in 'Nn':
        break
print('-=' * 16)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print(f'-' * 26)
for i, a in enumerate(ficha):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('*' * 30)
    opc = int(input('Notas de qual aluno deseja que eu mostre? 999 para interromper: '))
    if opc == 999:
        print('Encerrando...Volte sempre!!!')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc - 1][0]} são {ficha[opc][1]}...')
print('*' * 30)
print('**********VOLTE SEMPRE!**********')
