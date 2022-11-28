nome = input('Digite seu nome completo: ')
splitnome = nome.split()
nome_sem_espaço = len(nome.replace(' ', ''))


print('Seu nome com todas as letras maiusculas fica:', nome.upper())
print('Seu nome com todas as letras minusculas fica:', nome.lower())
print(f'Seu nome tem {nome_sem_espaço} caracteres sem contar os espaços')
print(
    f'E o seu primeiro nome é {splitnome[0]} e ele tem {len(splitnome[0])} letras')
