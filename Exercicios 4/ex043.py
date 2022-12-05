peso = float(input('Digite o seu peso em (KG): '))
altura = float(input('Digite sua altura em (M): '))
imc = peso / (altura ** 2)


if imc < 18.5:
    print(f'IMC de {imc:.2f}')
    print('Abaixo do peso')
elif imc < 25:
    print(f'IMC de {imc:.2f}')
    print('Peso ideal')
elif imc < 30:
    print(f'IMC de {imc:.2f}')
    print('Sobrepeso')
elif imc < 40:
    print(f'IMC de {imc:.2f}')
    print('Obesidade')
else:
    print(f'IMC de {imc:.2f}')
    print('Obesidade mórbida')
