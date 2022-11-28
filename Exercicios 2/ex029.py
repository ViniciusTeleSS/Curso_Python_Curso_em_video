velocidade = int(input('Digite a velocidade do carro em km/h: '))

if velocidade > 80:
    excedente = velocidade - 80
    multa = excedente * 7
    print('Você está multado por ultrapassar o limite de velocidade')
    print(f'O valor da multa é de: R${multa:.2f}')
else:
    print('Você passou dentro do limite de velocidade.')
