lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    cont = input('Deseja continuar [S/N]')
    if cont in 'Nn':
        break

print(f'Foram digitados {len(lista)} números')

print(f'A lista ordenada de forma decrescente fica {sorted(lista, reverse=True)}')

if 5 in lista:
    print('O valor 5 foi encontrado na lista')
else:
    print('O valor 5 foi não encontrado na lista')