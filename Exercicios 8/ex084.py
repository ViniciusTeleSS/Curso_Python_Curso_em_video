dados = []
galera = []
maior = 0 
menor = 0

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))

    if len(galera) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    galera.append(dados[:])
    dados.clear()

    cont = input('Quer continuar? [S/N] ')
    if cont in 'Nn':
        break
    
print('=-'*30)
print(f'Ao todo, você cadastrou {len(galera)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}]', end='') 
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')

