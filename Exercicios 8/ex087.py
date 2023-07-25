matriz = [[],[],[]]
pares = []
soma_ult_col = 0

for i in range(0,3):
    for c in range(0,3):
        matriz[i].append(int(input(f"Digite um valor para [{i},{c}]: ")))

print('-='*30)
for i in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[i][c]:^5}]', end='')
    print()

print('-='*30)
for sublista in matriz:
    for elemento in sublista:
        if elemento % 2 == 0:
            pares.append(elemento)

print(f'A soma dos valores pares é {sum(pares)}')

for sublista in matriz:
    ultimo_elemento = sublista[-1]
    soma_ult_col += ultimo_elemento

print(f'A soma dos valores da terceira coluna é {soma_ult_col}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')