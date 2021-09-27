def notas(*n, sit=False):
    """
    ->Função que analisa as notas de vários alunos
    :param n: notas,pode receber várias
    :param sit: mostra a situação dos alunos em relação ás notas
    :return: retorna um dicionário com todas as notas e situação da turma
    """
    r = {}
    r['total'] = len(n)
    r['menor'] = min(n)
    r['maior'] = max(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA!!!'
        elif r['media'] >= 5:
            r['situacao'] = 'Rázoável!'
        else:
            r['situacao'] = 'Ruim!'
    return r


resp = notas(4, 4.6, 5, 3.5, sit=True)
print(resp)
