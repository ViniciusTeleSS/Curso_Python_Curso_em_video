from random import randint

print('Bem vindo ao jogo do adivinha.')
print('-=-' * 25)
print('Tente adivinhar o número que eu pensei, dica: é um número inteiro entre 0 e 10')
print('-=-' * 25)

chute = int(input('Digite o numero: '))
numero = randint(0, 10)
tentativas = 1

while chute != numero:

    if chute < numero:
        chute = int(input('Maior, tente outra vez: '))
    else:
        chute = int(input('Menor, tente outra vez: '))
    tentativas += 1

print(f'Parabéns, você acertou eu pensei em {numero}')
print(f'Você precisou de {tentativas} tentativas')
