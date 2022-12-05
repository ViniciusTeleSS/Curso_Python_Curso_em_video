numero = []

for i in range(1, 6):
    peso = input(f'Digite o peso da {i}º pessoa: ')
    numero += [peso]

print(f'O maior peso foi:', max(numero))
print(f'O menor peso foi:', min(numero))
