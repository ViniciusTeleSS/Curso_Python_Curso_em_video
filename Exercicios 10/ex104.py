def leaiInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return n
        else: 
            print('ERRO! Digite um número inteiro válido')

        
print('-' * 30)
n = leaiInt('Digite um número: ')
print(f'Você digitou o número {n}')