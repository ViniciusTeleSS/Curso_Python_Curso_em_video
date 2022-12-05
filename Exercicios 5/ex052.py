num = int(input('Digite um numero: '))
tot = 0

for i in range(1, num + 1):
    if num % i == 0:
        tot += 1

if tot == 2:
    print(f'O numero {num} é primo')
else:
    print(f'O numero {num} não é primo')
