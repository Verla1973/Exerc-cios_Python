num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

print('*' * 35)
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print(f'O número {num} convertido para binário é {bin(num)[2:]}')
elif opcao == 2:
    print(f'O número {num} convertido para OCTAL é {oct(num)[2:]}')
elif opcao == 3:
    print(f'O número {num} convertido para HEXADECIMAL é {hex(num)[2:]}')
else:
    print('OPÇÃO INVÁLIDA...')
