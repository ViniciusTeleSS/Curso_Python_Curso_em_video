quilometragem = int(input('Digite a distância total da viagem em km: '))

if quilometragem > 200:
    valor = quilometragem * 0.45
    print(f'O valor da passagem será de {valor}')
else:
    valor = quilometragem * 0.50
    print(f'O valor da passagem será de {valor}')
