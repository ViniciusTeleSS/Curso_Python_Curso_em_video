from datetime import datetime

data = datetime.now()
maior = 0
menor = 0

for i in range(1, 8):
    nasci = int(input(f'Digite o ano de nascimento da {i}º pessoa: '))
    idade = data.year - nasci

    if idade >= 21:
        maior += 1
    else:
        menor += 1

print(f'De 7 pessoas, {maior} são de maior e {menor} são de menor')
