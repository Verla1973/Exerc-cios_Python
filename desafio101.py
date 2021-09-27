def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return print(f'Com {idade} anos, NÃO VOTA!!!')
    elif 16 <= idade < 18 or idade > 65:
        return print(f'Com {idade} anos, o VOTO É OPCIONAL!!!')
    else:
        return print(f'Com {idade} anos, o VOTO É OBRIGATÓRIO!!!')


nasc = int(input('Em que ano você nasceu? '))
voto(nasc)
