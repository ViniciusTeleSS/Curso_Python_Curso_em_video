def area(larg,compri):
    tot = larg * compri
    print(f'A area de um terreno {larg}x{compri} é de {tot}.')

print('CONTROLE DE TERRENOS')
print('-' * 30)

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l, c)