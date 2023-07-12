numeros = []
numeros_pares = []
numeros_impares = []

while True:
    n = int(input('Digite um número: '))
    numeros.append(n)

    cont = input('Deseja continuar? [S/N]')
    if cont in 'Nn':
        break

for i in numeros:
    if i % 2 == 0:
        numeros_pares.append(i)
    else:
        numeros_impares.append(i)

print('=-'*30)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {numeros_pares}')
print(f'A lista de impares é {numeros_impares}')
