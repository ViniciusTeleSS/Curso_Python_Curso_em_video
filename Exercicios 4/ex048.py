soma = 0
cont = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        cont += 1
        soma += i
print(f'A soma de todos os valores é {soma} e {cont} valores foram somados')
