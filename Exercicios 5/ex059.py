from time import sleep

carac = '-=-' * 20

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
opcao = 0


while opcao != '5':

    print(carac)
    print('''O que deseja fazer com esses valores? \n
    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NUMEROS
    [5]SAIR DO PROGRAMA
    ''')
    opcao = int(input('Qual a sua opção? '))

    if opcao == 1:
        soma = valor1 + valor2
        print(f'O resultado da soma entre {valor1} e {valor2} é {soma}')
        print(carac)

    elif opcao == 2:
        mult = valor1 * valor2
        print(
            f'O resultado da multiplicação entre {valor1} e {valor2} é {mult}')
        print(carac)

    elif opcao == 3:
        if valor1 > valor2:
            print(f'{valor1} é maior do que {valor2}')
            print(carac)

        elif valor1 == valor2:
            print(f'Os dois valores são iguais')
        else:
            print(f'{valor2} é maior do que {valor1}')
            print(carac)

    elif opcao == 4:
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite outro valor: '))

        print(carac)
    elif opcao == 5:
        break
    else:
        print('Opção inválida!')

print(carac)
print('Finalizando o programa!')
sleep(1)
print('FIM DO PROGRAMA!')
print(carac)
