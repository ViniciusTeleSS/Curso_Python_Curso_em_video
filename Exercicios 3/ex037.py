num = int(input('Digite um número inteiro: '))
base = input(
    'Agora, escolha a base para conversão: \n1-binário \n2-octagonal\n3-hexadecimal \n')


if base == '1':
    binario = format(num, 'b')
    print(f'Você escolheu binário, o {num} em binário é {binario}')
elif base == '2':
    octagonal = format(num, 'o')
    print(f'Você escolheu binário, o {num} octagonal é {octagonal}')
elif base == '3':
    hexadecimal = format(num, 'x')
    print(f'Você escolheu binário, o {num} hexagonal é {hexadecimal}')
else:
    print('Opção Inválida, por favor escolha uma das opções acima')
