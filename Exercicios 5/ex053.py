frase = str(input('Digite uma frase: ')).lower().strip()
palavras = frase.split()
junto = ''.join(palavras)
invertido = junto[::-1]

if junto == invertido:
    print('É palindromo')
else:
    print('Não é palindromo')
