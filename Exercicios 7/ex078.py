numeros = []
maior = 0
menor = 0

for posicao in range(0,5):
    numeros.append(int(input(f'Digite um numero para a posição {posicao}: ')))
    
    if posicao == 0:
        maior = menor = numeros[posicao]
    else:
        if numeros[posicao] > maior:
            maior = numeros[posicao]
        if numeros[posicao] < menor:
            menor = numeros[posicao]


print('=-'*20)    
print(f'Você digitou os valores {numeros}')
print(f'O MAIOR valor digitado foi {maior} nas posições ',end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}...', end='')

print(f'\nO MENOR valor digitado foi {menor} nas posições ',end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}...', end='')