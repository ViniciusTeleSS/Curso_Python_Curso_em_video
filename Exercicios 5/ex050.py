soma = 0
cont = 0

for i in range(0, 6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        cont += 1
        soma += num
print(
    f'A soma de todos os valores pares digitados é {soma} e foram somados {cont} valores')
