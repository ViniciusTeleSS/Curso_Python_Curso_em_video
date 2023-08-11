from time import sleep

def contador(inicio, fim, passo):

    if passo < 0:
        passo = abs(passo)
    elif passo == 0:
        passo = 1

    print('=-' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio > fim:
        for i in range(inicio, fim - 1, -passo):
            print(f'{i}', end=' ')
    else:
        for i in range(inicio, fim + 1, passo):
            print(f'{i}', end=' ')
    print()
    print('=-' * 30)

contador(1,10,1)
contador(10,0,2)

print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i,f,p)