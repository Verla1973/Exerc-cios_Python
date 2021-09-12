expres = str(input('Digite uma expressão: '))
pilha = []
for simbolo in expres:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida...')
else:
    print('Sua expressão é inválida...')
