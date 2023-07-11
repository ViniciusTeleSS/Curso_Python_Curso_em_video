lista = []

while True:
    n = int(input('Digite um valor: '))

    if n not in lista:
     print('Valor adicionado com sucesso...')
     lista.append(n)
    else:
       print('Valor duplicado! Não vou adicionar...')

    cont = input('Quer continuar? [S/N] ')
    if cont in 'Ss':
        continue
    else:
        break

print('=-'*30)
print(sorted(lista))