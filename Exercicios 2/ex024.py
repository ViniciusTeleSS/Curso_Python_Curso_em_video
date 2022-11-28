cidade = str(input('Digite o nome da sua cidade: ')).lower().strip()

splitcidade = cidade.split()

if splitcidade[0] == 'santo':
    print('O nome da sua cidade começa com Santo')
else:
    print('O nome da sua cidade não começa com Santo')
