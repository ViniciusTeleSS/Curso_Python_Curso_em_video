from time import sleep
from random import sample

print('=-' * 20)
print('JOGA NA MEGA SENA'.center(30))
print('=-' * 20)

jogos = []

qtd = int(input('Quantos jogos você quer que eu sorteie? '))

for i in range(0,qtd):
    jogos.append(sample(range(1,61),6))

print(f'SORTEANDO {qtd} JOGOS'.center(30))
print('=-' * 20)

for i in range(0,qtd):
    print(f'Jogo {i+1}: ', end='')
    print(sorted(jogos[i]))
    sleep(1)