from random import randint

numero = randint(0, 5)

print('Bem vindo ao jogo do adivinha.')
print('-=-' * 25)
print('Tente adivinhar o número que eu pensei, dica: é um número inteiro entre 0 e 5')
print('-=-' * 25)

chute = int(input('Digite o numero: '))

if chute == numero:
    print(f'Parabéns, você acertou, o número que eu pensei foi {numero}')
else:
    print(
        f'Não foi dessa vez, o número que eu pensei foi {numero} e não {chute}')
print('Fim de jogo')
