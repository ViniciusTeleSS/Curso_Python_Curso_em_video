n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
multi = n1 * n2
divisao = n1 / n2
divisaoexata = n1 // n2
potencia = n1 ** n2


print(f'A soma é {soma}, o produto {multi} e a multiplicação é {divisao:.3f}')
print(f'Divisão inteira {divisaoexata} e potência {potencia}')
