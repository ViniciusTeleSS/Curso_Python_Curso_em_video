numero = int(input("Fatorial de: "))

resultado = 1
count = 1
repet = numero + 1

print(f'{numero}! =', end=' ')

while count <= numero:
    resultado *= count
    count += 1
    repet -= 1
    print(f'{repet}x', end='')
print(f' = {resultado}')
