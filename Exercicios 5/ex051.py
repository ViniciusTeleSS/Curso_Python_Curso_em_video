inicio = int(input('Inicio: '))
passo = int(input('Passo: '))
decimo = inicio + (10 - 1) * passo

for i in range(inicio, decimo + passo, passo):
    print(f'{i} -> ', end=' ')
print('FIM')
