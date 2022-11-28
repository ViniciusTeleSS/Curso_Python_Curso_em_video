ano = int(input('Digite um ano para saber se ele é bissexto: '))

bissexto = ano % 4

if bissexto == 0:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')
