def factorial(n, show = False):
    """
    Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: Opcional,se mostra ou não os cálculos do fatorial
    :return: O valor do fatorial do número
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} ', end='')
            if c > 1:
                print('X ', end='')
            else:
                print('= ', end='')
        f *= c
    return f


n = int(input('Digite o número que deseja o fatorial de qual número: '))
res = str(input('Você deseja os calculos juntos? ')).strip().upper()[0]
if res  in 'S':
    r = True
else:
    r = False
print(factorial(n, show = r))
help(factorial)
