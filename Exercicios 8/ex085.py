lista = [[],[]]

for i in range(1,8):
    n = int(input(f'Digite o {i}º valor: '))
    
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

print('=-'*30)
print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores impares digitados foram: {sorted(lista[1])}')