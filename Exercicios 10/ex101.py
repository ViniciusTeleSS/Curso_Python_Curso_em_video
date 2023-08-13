def voto(a):
    from datetime import datetime

    ano_atual = datetime.now().year
    idade = ano_atual - ano

    if idade < 65 and idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade > 65 or idade >= 16:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: NÃO VOTA.'


print('-' * 30)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))

